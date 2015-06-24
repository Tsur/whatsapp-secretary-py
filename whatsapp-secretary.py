#/bin/env python

import logging
import sys
import getopt
import os
from layer import secretary
from config import load
from yowsup.layers.auth import YowAuthenticationProtocolLayer
from yowsup.layers.protocol_messages import YowMessagesProtocolLayer
from yowsup.layers.protocol_receipts import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks import YowAckProtocolLayer
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.coder import YowCoderLayer
from yowsup.layers.axolotl import YowAxolotlLayer
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup.stacks import YowStack, YOWSUP_CORE_LAYERS
from yowsup import env

def main(argv):

    phone = None
    password = None
    config = None

    try:

      opts, args = getopt.getopt(argv, "u:c:d", ["user=", "config=", "debug="])

    except getopt.GetoptError:

      print 'whatsapp-secretary.py -u <phone:password> -c <config> -d <debug>'
      sys.exit(2)

    for opt, arg in opts:

      if opt in ("-u", "--user"):

         user = arg.split('.')
         phone = user[0]
         password = user[1]

      elif opt in ("-c", "--config"):

         config = load(os.path.abspath(arg))

      elif opt in ("-d", "--debug"):

          logging.basicConfig(level=logging.CRITICAL)

    run(phone, password, config)


def run(phone, password, config):

    CREDENTIALS = (phone, password)

    layers = (
        secretary(config),
        (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer, YowReceiptProtocolLayer, YowAckProtocolLayer),
        YowAxolotlLayer,
    ) + YOWSUP_CORE_LAYERS

    stack = YowStack(layers)

    # Setting credentials
    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)

    # Whatsapp server address
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])

    # Info about us as WhatsApp client
    stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)              
    stack.setProp(YowCoderLayer.PROP_RESOURCE, env.CURRENT_ENV.getResource())

    # Sending the connect signal
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

    stack.loop()

if __name__ == "__main__":
    main(sys.argv[1:])

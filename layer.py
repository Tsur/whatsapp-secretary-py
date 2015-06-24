from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from utils import display

def secretary(config):

    class MessageLogic(YowInterfaceLayer):

        @ProtocolEntityCallback("message")
        def onMessage(self, message):

            self.ack(message)

            display(message, config)

        def ack(self, message):

            # Ack Received Message
            self.toLower(OutgoingReceiptProtocolEntity(message.getId(), message.getFrom()))

    return MessageLogic

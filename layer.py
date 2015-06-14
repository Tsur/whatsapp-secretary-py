import os, sys, json
from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv
    
def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

Config = None
    
if not Config:

    path = os.path.abspath(sys.argv[1])

    with open(path) as data_file:    
        Config = json.load(data_file, object_hook=_decode_dict)


class Layer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, message):

        self.ack(message)

        self.display(self.filter(message))

    def ack(self, message):

        # Ack Received Message
        self.toLower(OutgoingReceiptProtocolEntity(message.getId(), message.getFrom()))

    def filter(self, message):

        rules = self.getRules(message.getFrom())

        text = self.getText(message)

        return text if self.accepted(rules, text) else None

    def getText(self, message):

        if message.getType() == "text":
            return self.getTextMessageBody(message)
        elif message.getType() == "media":
            return self.getMediaMessageBody(message)
        else:
            return "Unknown message type %s " % message.getType()

    def getRules(self, sender):

        return Config.get(sender, None)

    def accepted(self, rules, text):
        
        return True

    def getTextMessageBody(self, message):
        return message.getBody()

    def getMediaMessageBody(self, message):
        if message.getMediaType() in ("image", "audio", "video"):
            return self.getDownloadableMediaMessageBody(message)
        else:
            return "[Media Type: %s]" % message.getMediaType()
       

    def getDownloadableMediaMessageBody(self, message):
         return "[Media Type:{media_type}, Size:{media_size}, URL:{media_url}]".format(
            media_type = message.getMediaType(),
            media_size = message.getMediaSize(),
            media_url = message.getMediaUrl()
            )
    
    def display(self, message):

        if message:

            #text = messageProtocolEntity.getBody()
            #user = messageProtocolEntity.getFrom()
            #id = messageProtocolEntity.getId()

            print("Got new message {}".format(message))

            # TODO: check text, user and id are strings

import re

def filter_message(message, config):

    if not message:
        return False

    return accepted(get_rules(message.getFrom(), config), get_text(message))

def get_text(message):

    if message.getType() == "text":
        return get_text_message_body(message)

    elif message.getType() == "media":
        return get_media_message_body(message)

    else:
        return "Unknown message type %s " % message.getType()

def get_rules(sender, config):

    return config.get(re.sub(r"\@.*$", "", sender), None) or config.get("*", None)

def accepted(rules, text):

    if not rules or not text:
        return False

    if rules is "*":
        return True

    only = rules.get('only', None)

    if only:

        if type(only) is not str:
            return any([word.lower() in text.lower() for word in only])

        return only.lower() in text.lower()

    return False

def get_text_message_body(message):

    return message.getBody()

def get_media_message_body(message):

    if message.getMediaType() in ("image", "audio", "video"):
        return get_downloadable_media_message_body(message)
    else:
        return "[Media Type: %s]" % message.getMediaType()

def get_downloadable_media_message_body(message):
     return "[Media Type:{media_type}, Size:{media_size}, URL:{media_url}]".format(
        media_type = message.getMediaType(),
        media_size = message.getMediaSize(),
        media_url = message.getMediaUrl()
        )

def display(message, config):

    if filter_message(message, config):

        print("{}".format(message))

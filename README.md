# Whatsapp-secretary

Tell your whatsapp secretary to just let you know what's important for you.

Note: This is very much a work in progress. It may not work as expected.

# Why

As a developer, I'm working too many hours with a text editor and several terminal sessions. In Europe, but specially in Spain, whatsapp is a very popular application, a must have, basically because all of your friends and relatives have it. It becomes very annoying to be interrupted every minute for some friend who has to tell me something not important and do not even say anything about all those groups chats bubbling up whatsapp notifications each 10 seconds just to end up reading nonsenses. It may be better to just disable notifications and you are done, yeah, but then you have no way to know when something you are really interesting on has been said, and even more, a context switch is required in the mind from your keyboard to the phone similar to what happens when using keyboard and mice, so with whatsapp-secretary you just need to have a look at your terminal session and do not need to be enabling/disabling notifications on your phone since whenever you start using whatsapp-secreatary, notifications will stop coming in your phone and will start coming in once you stop whatsapp-secretary.

# Setting up

Now create a config.json file as below:

```js
{
    "PHONE_NUMBER": {

      "only": ["word1", "word2"],
      "redirect": ["REDIRECT_TO_PHONE"]

    },

    "PHONE_NUMBER2": {

      "ignore": ["word1", "word2"],
      "autorespond": ["very busy man!, talk to me later"]

    },

    "GROUP_ID1": {

      "ignore": ["word1", "word2"]

    }
}
```

And finally just run it:

```bash
python ./whatsapp-secretary -c config.json -u "phone:password"
```

## Troubleshooting

> TypeError: Incorrect padding

This might fails cause of an incorrect password, check it ends with a "=" character. This type error is raised by base64.b64decode(pb64) at line 34 in file yowsup/layers/auth/layer_authentication.py, method __getCredentials, yowsup2 version 2.3.123, b64decode(pb64) calls binascii.a2b_base64(password). Try a python session, then import binascii, and make sure binascii.a2b_base64(password) does not raises any error.

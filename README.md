# Whatsapp-secretary

Tell your whatsapp secretary to just let you know what's important for you.

Note: This is very much a work in progress. It may not work as expected.

# Setting up

```bash
pip install -r requirements
```

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
./whatsapp-secretary.py -c config.json -u "user:password"
```

## Troubleshooting

> TypeError: Incorrect padding

This might fails cause of an incorrect password, check it ends with a "=" character. This type error is raised by base64.b64decode(pb64) at line 34 in file yowsup/layers/auth/layer_authentication.py, method __getCredentials, yowsup2 version 2.3.123, b64decode(pb64) calls binascii.a2b_base64(password). Try a python session, then import binascii, and make sure binascii.a2b_base64(password) does not raises any error.

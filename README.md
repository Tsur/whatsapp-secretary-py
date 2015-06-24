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
./whatsapp-secretary.py -c config.json -u user:password
```

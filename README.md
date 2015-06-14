# Whatsapp-secretary

Tell your whatsapp secretary to just let you know what's important for you.

# Setting up

```bash
pip install -r requirements
```

Now create a config.json file as below:

```js
{
  "phone": "YOUR_PHONE",
  "password": "YOUR_PASSWORD",
  "secretary": {

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
}
```

And finally just run it:

```bash
./whatsapp-secretary.py config.json
```
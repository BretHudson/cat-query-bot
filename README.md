# Cat Query Bot

This is a Twitter bot ([@CatQueryBot](https://twitter.com/CatQueryBot)) written in Python that receives words, queries the Google Custom Search Engine API, and then tweets the top 4 photos to an account if any are found, alone with the search query and the total amount of results.

## Setup

So, you want to clone it and create your own? Sure thing!

* Clone this repo
* Make a copy of the `local_settings_example.py` file and name it `local_settings.py` - instructions for each are listed below

## Getting Google API keys & Custom Search Engine ID

First things first, visit Google's [Custom Search Engine console](https://cse.google.com) to get started. Click "Add" and follow the instructions. Then, when you're done, you can set it to search the entire web with the following excerpt from [this Google Support topic](https://support.google.com/customsearch/answer/4513886?hl=en&ref_topic=4513742):

To set an existing search engine to search the entire web: 
- From the control panel, select the search engine you want to edit. 
- Click Setup from the menu on the left and then click the Basics tab. 
- Go to the Search the Entire Web section and toggle this feature On or Off.
- Selecting On will augment your results with general Web Search results. Selecting Off will limit your results only to the sites you specified.

You will also need to [enable image search](https://support.google.com/customsearch/answer/2630972?hl=en). Optional: adjust [SafeSearch](https://support.google.com/customsearch/answer/9115386?hl=en) settings.

## Twitter Developer API

Head on over to the [Twitter Developer Platform](https://developer.twitter.com/content/developer-twitter/en.html) website and fill out an application. Feel free to [contact me](https://twitter.com/BretHudson) if you're having issues getting your application accepted - I had to message back and forth for a little while before I got in with this particular bot.

Once you're in, create a new API project and generate some keys. Consult Google if you need help with this step.

## Configuring

The bot is written to read in from a local_settings.py file that stores API keys, links to feeds, and debug variables.

```
SAFE_SEARCH = True
```

Set safe search to True/False depending on if you're looking to keep NSFW images out of your feed.

```
GOOGLE_API_KEY = 'Your Google API Key'
GOOGLE_CUSTOM_SEARCH_ID = 'Your Google Custom Search Engine ID'
```

Plug in your Google API keys from earlier!

```
MY_CONSUMER_KEY = '57axlM8Ti5ntN8aOiGXu7lx48'
MY_CONSUMER_SECRET = 'mgK4pyeCwUmI6So3XxQIEmKqE70w7wKvRxKYrAJthPr7J1396O'
MY_ACCESS_TOKEN_KEY = '3171134888-3fLCSwWWP8j3PAQkflR0OfjVklLr5QN1VadOLVL'
MY_ACCESS_TOKEN_SECRET = 'lvROpdTFXViRJHE02es3vgabaMxAqJ19gAD3SuyPh8hrM'
```

Plug in your Twitter API keys from earlier!

```
WORDS_URL = ""
```

This URL is something you'll need to set up on your own. I simply created a PHP script on my website that allows me to send a GET request, and it sends back a JSON response that looks like one of the following:

```
{ success: true, word: 'sniper' }
{ success: false, word: null }
```

When you design this script, it must return a JSON string matching that format.

```
TEST_SCRAPE_URL = False
```

Since the Google Custom Search Engine has a rate limit, you probably don't want to query it hundreds of times while testing. Because of this, you can set TEST_SCRAPE_URL to a static page containing the results of a search (which you can copy/paste from the console after running!)

```
Debug = True
```

This ensures that the bot does not tweet while testing to make sure everything works. Set this to False when you're ready to deploy your bot!

## Credit

Thanks to both [Google](https://www.google.com) and [Twitter](https://twitter.com) for creating and maintaining great and simple to use APIs. Without them, this completely pointless project would have never seen the light of day.

I first got started with fiddling with Twitter bots thanks to [Tom Meagher](http://www.tommeagher.com/)'s [heroku_ebooks](https://github.com/tommeagher/heroku_ebooks). Check that repository out, and feel free to message me if you want some tips on how to implement some of the modifications I've made to it for [@bret_ebooks](https://twitter.com/bret_ebooks).

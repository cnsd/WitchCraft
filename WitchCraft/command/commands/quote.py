#quote.py
from configs.config import MessageType, MASHAPE_KEY
from configs.functions import botprint

import requests
import json

def quote():
	response = requests.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous",
	  headers={
	    "X-Mashape-Key": MASHAPE_KEY,
	    "Content-Type": "application/x-www-form-urlencoded",
	    "Accept": "application/json"
	  }
	)
	json_string = response.text
	response_as_dict = json.loads(json_string)
	quote = response_as_dict['quote']
	author = response_as_dict['author']
	botprint('`%s` -%s' % (quote, author), MessageType.INFO)
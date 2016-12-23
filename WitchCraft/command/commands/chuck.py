#chuck.py
from configs.config import MessageType, MASHAPE_KEY
from configs.functions import botprint

import requests
import json

def chuck():
	response = requests.get("https://matchilling-chuck-norris-jokes-v1.p.mashape.com/jokes/random?category=explicit",
	  headers={
	    "X-Mashape-Key": MASHAPE_KEY,
	    "Accept": "application/json"
	  }
	)
	json_string = response.text
	response_as_dict = json.loads(json_string)
	chuck_quote = response_as_dict['value']
	botprint('%s' % (chuck_quote), MessageType.INFO)
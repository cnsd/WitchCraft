#weather.py

from configs.config import MessageType, MASHAPE_KEY
from configs.functions import botprint


import requests
import json
import re

COORDS_PATTERN = '^\-?[0-9]{1,3}(\.[0-9]{1,6})?'

def weather(args):
	latitude = re.match(COORDS_PATTERN, args[0])
	longtitude = re.match(COORDS_PATTERN, args[1])

	if latitude and longtitude:
		json_string = requests.get("https://simple-weather.p.mashape.com/weatherdata?lat=%s&lng=%s" % (latitude.group(0), longtitude.group(0)),
	  							headers={
	    							"X-Mashape-Key": MASHAPE_KEY,
	    							"Accept": "application/json"
	  							}
								).text
		response_as_dict = json.loads(json_string)

		if (response_as_dict['query']['count']):

			date = response_as_dict['query']['results']['channel']['item']['condition']['date']
			temp = response_as_dict['query']['results']['channel']['item']['condition']['temp']
			temp_unit = response_as_dict['query']['results']['channel']['units']['temperature']
			text = response_as_dict['query']['results']['channel']['item']['condition']['text']
			city = response_as_dict['query']['results']['channel']['location']['city']
			country = response_as_dict['query']['results']['channel']['location']['country']

			forecast_low = response_as_dict['query']['results']['channel']['item']['forecast'][1]['low']
			forecast_high = response_as_dict['query']['results']['channel']['item']['forecast'][1]['high']
			forecast_text = response_as_dict['query']['results']['channel']['item']['forecast'][1]['text']
			
			botprint('According to: %s\n\
                     The weather in %s, %s is %s (%s%s).\n\
                     Tomorrow will be %s with %s%s to %s%s.' % (date, country, city, text, temp, temp_unit, forecast_text, forecast_low, temp_unit, forecast_high, temp_unit), MessageType.SUCCESS)
		else:
			botprint('Theres no data for the coords %s.' % args, MessageType.CRITICAL)

	else:
		botprint('The input %s is invalid.' % args, MessageType.ERROR)
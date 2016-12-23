#dox.py

from configs.config import MessageType
from configs.functions import botprint
from module.modules import emails

import re
import json
import requests

IP_PATTERN = "^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
EMAIL_PATTERN = "^[a-zA-Z0-9\.\-\_]{1,18}\@[a-zA-Z0-9\.\-\_]{1,18}\.(zw|zr|zm|za|yu|yt|ye|xxx|ws|wf|web|vu|vn|vi|vg|ve|vc|va|uy|us|um|uk|ug|ua|tz|tw|tv|tt|travel|tr|tp|to|tn|tm|tl|tk|tj|th|tg|tf|tel|td|tc|sz|sy|sv|su|store|st|ss|sr|so|sn|sm|sl|sk|sj|si|sh|sg|se|sd|sch\.uk|sc|sb|sa|rw|ru|ro|re|qa|py|pw|pt|ps|pro|pr|post|pn|pm|plc\.uk|pl|pk|ph|pg|pf|pe|pa|org\.uk|org|om|nz|nu|nt|nr|np|nom|no|nl|ni|nhs\.uk|ng|nf|net\.uk|net|ne|nc|nato|name|na|mz|my|mx|mw|mv|museum|mu|mt|ms|mr|mq|mp|mod\.uk|mobi|mo|mn|mm|ml|mk|mil|mh|mg|me\.uk|me|md|mc|ma|ly|lv|lu|ltd\.uk|lt|ls|lr|lk|li|lc|lb|la|kz|ky|kw|kr|kp|kn|km|ki|kh|kg|ke|jp|jobs|jo|jm|je|it|is|ir|iq|io|int|info|in|im|il|ie|id|hu|ht|hr|hn|hm|hk|gy|gw|gu|gt|gs|gr|gq|gp|gov\.uk|gov|gn|gm|gl|gi|gh|gf|ge|gd|gb|ga|fx|fr|fo|fm|fk|fj|firm|fi|eu|et|es|er|eh|eg|ee|edu|ec|dz|do|dm|dk|dj|de|dd|cz|cy|cx|cv|cu|cs|cr|coop|com|co\.uk|co|cn|cm|cl|ck|ci|ch|cg|cf|cd|cc|cat|ca|bz|by|bw|bv|bt|bs|br|bo|bn|bm|bj|biz|bi|bh|bg|bf|be|bd|bb|ba|az|ax|aw|au|at|asia|as|arpa|ar|aq|ao|an|am|al|ai|ag|af|aero|ae|ad|ac\.uk|ac)"

def fetch_ip_whois(json_string):
	response_as_dict = json.loads(json_string)
	if (response_as_dict['status'] == 'success'):
		response_string = 'Country: %s\n\
		     Region: %s\n\
		     City: %s\n\
		     ZIP: %s\n\
		     ISP: %s\n\
		     Organization: %s\n\
		     Latitude: %s\n\
		     Longtitude: %s\n\
		     IP: %s\
				  ' % (response_as_dict['country'],
						response_as_dict['regionName'],
						response_as_dict['city'],
						response_as_dict['zip'],
						response_as_dict['isp'],
						response_as_dict['org'],
						response_as_dict['lat'],
						response_as_dict['lon'],
						response_as_dict['query'])
	else:
		response_string = 'Error: %s' % response_as_dict['message']

	return response_string

def dox(args):
	user_input = args[0]
	ip = re.match(IP_PATTERN, user_input)
	email = re.match(EMAIL_PATTERN, user_input)

	if ip:
		botprint('IP Detected.', MessageType.DEBUG)
		botprint('Searching info about (%s)...' % ip.group(0), MessageType.INFO)
		json_string = requests.get("http://ip-api.com/json/"+ip.group(0)).text
		formatted_whois_response = fetch_ip_whois(json_string)
		if formatted_whois_response[0] == 'C':
			botprint(formatted_whois_response, MessageType.SUCCESS)
		else:
			botprint(formatted_whois_response, MessageType.ERROR)

	elif user_input == 'me':
		json_string = requests.get("http://ip-api.com/json/").text
		formatted_whois_response = fetch_ip_whois(json_string)
		if formatted_whois_response[0] == 'C':
			botprint(formatted_whois_response, MessageType.SUCCESS)
		else:
			botprint(formatted_whois_response, MessageType.ERROR)

	elif email:
		botprint('Email Detected.', MessageType.DEBUG)
		botprint('Searching info about (%s)...' % email.group(0), MessageType.INFO)
		mailtester_function_result = emails.get_mailtester_data(email.group(0))
		if mailtester_function_result[0] == 'E':
			botprint(mailtester_function_result, MessageType.SUCCESS)
		elif mailtester_function_result[0] == 'S':
			botprint(mailtester_function_result, MessageType.WARNING)
		elif mailtester_function_result[0] == 'T':
			botprint(mailtester_function_result, MessageType.ERROR)
		else:
			botprint('Unknown Error', MessageType.CRITICAL)


	else:
		botprint('`%s` is a bad input.' % user_input, MessageType.ERROR)

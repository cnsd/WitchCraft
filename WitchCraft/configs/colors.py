#colors.py
from __future__ import print_function
from colorama import init
from colorama import Fore, Back, Style

init()

def get_color_format(message_type):
	'''
	class MessageType(Enum):
	NORMAL = -1
	SUCCESS = 0
	INFO = 1
	WARNING = 2
	ERROR = 3
	CRITICAL = 4
	DEBUG = 5
	'''
	if (message_type == 0):
		return ([Fore.GREEN, '[SUCC]'])
	elif (message_type == 1):
		return ([Fore.CYAN, '[INFO]'])
	elif (message_type == 2):
		return ([Fore.YELLOW, '[WARN]'])
	elif (message_type == 3):
		return ([Fore.RED, '[ERR ]'])
	elif (message_type == 4):
		return ([Fore.WHITE + Back.RED, '[CRIT]'])
	elif (message_type == 5):
		return ([Fore.CYAN + Style.DIM, '[DEBG]'])
	elif (message_type == -1):
		return ([Fore.WHITE, '[NORM]'])
	else:
		return ('How did you get here..?')

def reset_style():
	print (Style.RESET_ALL, end="")

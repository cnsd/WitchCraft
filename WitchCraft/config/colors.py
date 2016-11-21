#colors.py
from __future__ import print_function
from config import *
import config
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
	'''
	if (message_type == config.MessageType.SUCCESS):
		return ([Fore.GREEN, '[SUCC]'])
	elif (message_type == config.MessageType.INFO):
		return ([Fore.CYAN, '[INFO]'])
	elif (message_type == config.MessageType.WARNING):
		return ([Fore.YELLOW, '[WARN]'])
	elif (message_type == config.MessageType.ERROR):
		return ([Fore.RED, '[ERR ]'])
	elif (message_type == config.MessageType.CRITICAL):
		return ([Fore.WHITE + Back.RED, '[CRIT]'])
	elif (message_type == config.MessageType.NORMAL):
		return ([Fore.WHITE, '[NORM]'])
	else:
		return ('How did you get here..?')

def reset_style():
	print (Style.RESET_ALL, end="")

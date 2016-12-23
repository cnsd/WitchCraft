#hello.py
from configs.config import MessageType
from configs.functions import botprint

def hello(args):
	if (args[0] != ''):
		return ('Hello %s, I\'m WitchCraft!' % args[0])
	else:
		botprint('YDB Your input is wrong', MessageType.CRITICAL)
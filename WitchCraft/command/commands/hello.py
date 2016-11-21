#hello.py
import config.config as config
from config.config import *

def hello(args):
	if (args[0] != ''):
		return ('Hello %s, I\'m WitchCraft!' % args[0])
	else:
		botprint('YDB Your input is wrong', MessageType.ERROR)
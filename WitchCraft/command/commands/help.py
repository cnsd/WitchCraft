#help.py
#IMPORTS
import os
import glob

from configs.config import MessageType
from configs.functions import botprint

SPACING = '		        '

def help():
	commands = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+'/*.py')]
	commands_list = ''
	for i in range(len(commands) - 1):
		commands_list += (SPACING + '[*] ' + commands[i] + '\n')

	botprint("The available commands are: \n%s" % commands_list, MessageType.INFO)
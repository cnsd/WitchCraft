#main.py
import requests

import configs.config as config
import configs.colors as colors
import command.command_handler as command_handler

from command.command_headers import *
from command.commands import chuck

from configs.config import *
from configs.colors import *
from configs.functions import botprint

from os import system
system("title "+config.PREFIX+" Version "+config.VERSION)
system("cls")

'''
Main function
'''
def main():
	chuck.chuck()
	print '' #Spacer
	while (True):
		botprint('', MessageType.NORMAL, True)
		command = raw_input()
		execute_command(command)


def execute_command(user_input):
	command = user_input.split(' ')[0]
	if command_handler.is_valid_command(user_input) or command_handler.is_valid_command(command):
		if command_handler.check_has_correct_args(user_input, command):
			args = user_input.split(' ')
			del args[0]
			result = command_handler.pass_to_function(command, args)
			if result:
				botprint('%s' % (result), MessageType.INFO)
		else:
			#Todo: Print a Usage message, create a function that will build the message dynamically from command_headers like check_has_correct_args works.
			botprint(('The command `%s` requires %d arguments. You gave %d.' % (command, int(commands[command]['argc']), len(user_input.split(' ')) - 1)), MessageType.WARNING)
	elif command == '':
		None #Do nothing
	else:
		botprint(('The command `%s` is invalid!' % command), MessageType.ERROR)




'''
Main run
'''

if __name__ == "__main__":
	print ENTER_SCREEN
	main()

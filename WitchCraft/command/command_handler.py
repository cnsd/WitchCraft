#handle_commands.py
from commands import *
from command_headers import *

import importlib

def is_valid_command(command):
	if command in commands:
		return True

def check_has_args(command):
	if 'argc' in commands[command]:
		return True

def check_has_correct_args(user_input, command):
	user_input = user_input.split(' ')
	if len(user_input) - 1 == commands[command]['argc']:
		return True

def pass_to_function(command, args):
	module = importlib.import_module('command.commands.%s' % command)
	function = getattr(module, command)

	if args:
		# need to reference to src.lib.commands.<command
		return function(args)
	else:
		# need to reference to src.lib.commands.<command
		return function()
#handle_modules.py
from modules import *
from module_headers import *

import importlib

def is_valid_module(module):
	if module in modules:
		return True

def check_has_args(module):
	if 'argc' in modules[module]:
		return True

def check_has_correct_args(user_input, module):
	user_input = user_input.split(' ')
	if len(user_input) - 1 == modules[module]['argc']:
		return True

def pass_to_function(module, args):
	module = importlib.import_module('module.modules.%s' % module)
	function = getattr(module, module)

	if args:
		# need to reference to src.lib.modules.<module
		return function(args)
	else:
		# need to reference to src.lib.modules.<module
		return function()
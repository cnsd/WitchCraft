#FUNCTIONS
from __future__ import print_function
from config import MessageType, colors, PROMPT

def botprint(string, msgtype = MessageType.NORMAL, stay_in_line = False):
	color_return_value = colors.get_color_format(msgtype.value)
	if (stay_in_line):
		print ((color_return_value[0] + color_return_value[1] + ' ' + PROMPT + string), end="")
	else:
		print (color_return_value[0] + color_return_value[1] + ' ' + PROMPT + string)
	colors.reset_style()
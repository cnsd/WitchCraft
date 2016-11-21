#config.py
from __future__ import print_function
from enum import Enum
import colors as colors
from colors import *

#Configs
PREFIX = 'WitchCraft'
VERSION = '0.0.1'

#GLOBAL VARIABLES

USERAGENT = 'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0'
HOST = 'www.fxp.co.il'
COOKIES = 'pagenumber=1546; bb_userid=3337730; bb_password=a71c0023822ea108ae751b0c5b44a661;'

PROMPT = PREFIX + ' >> '

ENTER_SCREEN = Fore.GREEN + """
 __    __ _ _       _       ___           __ _   
/ / /\ \ (_) |_ ___| |__   / __\ __ __ _ / _| |_ 
\ \/  \/ / | __/ __| '_ \ / / | '__/ _` | |_| __|
 \  /\  /| | || (__| | | / /__| | | (_| |  _| |_ 
  \/  \/ |_|\__\___|_| |_\____/_|  \__,_|_|  \__|
--Coded By cnsd. 2016--
""" + Fore.RESET + """
Welcome to """ + PREFIX + """!
Type `help` to see the help message.
"""

#CLASSES

'''
ScrapeTypes Enum
'''
class ScrapeType(Enum):
	forum = 1
	thread = 2


'''
ScrapeTargets Enum
'''
class ScrapeTarget(Enum):
	titles = 1
	common_opener = 3

	comments = 2
	common_replier = 4


'''
Botprint Message Types Enum
'''
class MessageType(Enum):
	NORMAL = -1
	SUCCESS = 0
	INFO = 1
	WARNING = 2
	ERROR = 3
	CRITICAL = 4



#FUNCTIONS

def botprint(str, type = MessageType.NORMAL, stay_in_line = False):
	color_return_value = colors.get_color_format(type)
	if (stay_in_line):
		print ((color_return_value[0] + color_return_value[1] + ' ' + PROMPT + str), end="")
	else:
		print (color_return_value[0] + color_return_value[1] + ' ' + PROMPT + str)
	colors.reset_style()


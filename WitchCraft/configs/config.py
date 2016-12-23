#config.py

# #IMPORTS
from enum import Enum
import colors as colors
from colors import *
from command.command_headers import commands
from module.module_headers import modules

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
    DEBUG = 5

# #CONSTANTS

#Configs
PREFIX = 'WitchCraft'
VERSION = '0.0.1'
MASHAPE_KEY = 'oLe8LLCp2pmsh4umUCfo48arCC2vp1T2G0FjsnRifq2n8Aalb6'

PROMPT = PREFIX + ' >> '


AVAILABLE_COMMANDS = len(commands)
AVAILABLE_MODULES = len(modules)

#ENTER_SCREEN = 'DEBUG'
ENTER_SCREEN = """%s
 __    __ _ _       _       ___           __ _   
/ / /\ \ (_) |_ ___| |__   / __\ __ __ _ / _| |_ 
\ \/  \/ / | __/ __| '_ \ / / | '__/ _` | |_| __|
 \  /\  /| | || (__| | | / /__| | | (_| |  _| |_ 
  \/  \/ |_|\__\___|_| |_\____/_|  \__,_|_|  \__|
--Credits go here 2016--
%s
Welcome to %s!
Type `help` to see the help message.
%s
[%d] Available commands.
[%d] Available modules.
%s""" % (Fore.MAGENTA, Fore.RESET, PREFIX, Fore.CYAN + Style.DIM, AVAILABLE_COMMANDS, AVAILABLE_MODULES, Fore.RESET + Style.RESET_ALL)

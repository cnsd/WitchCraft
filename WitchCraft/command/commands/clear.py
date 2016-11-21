#clear.py
import os
from config.colors import *
from config.config import *

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
	print ENTER_SCREEN
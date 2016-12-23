#clear.py
import os
from configs.config import ENTER_SCREEN
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
	print ENTER_SCREEN
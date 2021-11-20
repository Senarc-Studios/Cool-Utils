import os
import sys
from dotenv import find_dotenv, load_dotenv

def get_env(variable: str):
	try:
		load_dotenv(find_dotenv())
		value = os.getenv[f"{variable}"]
		if value is not "":
			return value
		else:
			return None
	except:
		return None

def get_command(command: str):
	PYTHON = {
		'linux': 'python3',
		'win32': 'python',
		'macos': 'python3'
	}

	PIP = {
		'linux': 'python3 -m pip',
		'win32': 'pip',
		'macos': 'python3 -m pip'
	}

	CLEAR = {
		'linux': 'clear',
		'win32': 'cls',
		'macos': 'clear'
	}

	LS = {
		'linux': 'ls',
		'win32': 'dir',
		'macos': 'ls'
	}
	command = command.lower()
	if command == "python":
		return PYTHON[sys.platform]

	elif command == "pip":
		return PIP[sys.platform]

	elif command == "clear":
		return CLEAR[sys.platform]

	elif command == "ls":
		return LS[sys.platform]

	else:
		return command
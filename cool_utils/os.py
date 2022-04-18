"""
BSD 3-Clause License

Copyright (c) 2021-present, BenitzCoding
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import os
import sys
from datetime import datetime, tzinfo
from typing import TypeVar

__all__ = (
	'Terminal'
)

T = TypeVar('T', bound='Terminal')


def get_command(command: str):
	PYTHON = {
		'linux': 'python3',
		'win32': 'py',
		'macos': 'python3'
	}

	PIP = {
		'linux': 'python3 -m pip',
		'win32': 'py -m pip',
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

	OPTIONS = {
		"python": PYTHON,
		"pip": PIP,
		"clear": CLEAR,
		"ls": LS
	}

	command_lower = command.lower()
	try:
		return OPTIONS[command_lower][sys.platform]
	except:
		return command


BOLD = "\033[1m"
FAIL = "\033[91m"
WARNING = "\033[93m"
WHITE = "\33[97m"
RESET = "\033[0m"


class Terminal:
	format = "%d-%m-%Y | %H:%M:%S"
	log = False
	log_file = None
	error_func = None

	@staticmethod
	def set_format(format: str):
		Terminal.format = format

	@staticmethod
	def start_log(name: str = None):
		Terminal.log = True
		name = name or "latest"
		Terminal.log_file = name

	@staticmethod
	def stop_log():
		Terminal.log = False
		Terminal.log_file = None

	@staticmethod
	def display(content):
		time = datetime.now()
		if Terminal.log is True:
			file = open(f"{Terminal.log_file}.log", "a")
			file.write(time.strftime(f"[{Terminal.format}] INFO: ") + f"{content}" + "\n")
		print(BOLD + WHITE + time.strftime(f"[{Terminal.format}] INFO: ") + RESET + WHITE + f"{content}" + RESET)

	@staticmethod
	def warn(content):
		time = datetime.now()
		if Terminal.log is True:
			file = open(f"{Terminal.log_file}.log", "a")
			file.write(time.strftime(f"[{Terminal.format}] WARNING: ") + f"{content}" + "\n")
		print(BOLD + WARNING + time.strftime(f"[{Terminal.format}] WARNING: ") + RESET + WARNING + f"{content}" + RESET)

	@staticmethod
	def error(content):
		time = datetime.now()
		if Terminal.log is True:
			file = open(f"{Terminal.log_file}.log", "a")
			file.write(time.strftime(f"[{Terminal.format}] ERROR: ") + f"{content}" + "\n")
		print(BOLD + FAIL + time.strftime(f"[{Terminal.format}] ERROR: ") + RESET + FAIL + f"{content}" + RESET)
		if Terminal.error_func is not None:
			return Terminal.error_func()

	@staticmethod
	def on_error(function) -> None:
		Terminal.error_func = function
		return None

	@staticmethod
	def clear():
		os.system(get_command("clear"))

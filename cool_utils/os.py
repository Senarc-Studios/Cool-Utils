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
from datetime import datetime

def get_command(command: str):
	WIN_COMMANDS = {
		"python": "python",
		"pip": "python -m pip",
		"ls": "dir",
		"clear": "cls"
	}

	UNIX_COMMANDS = {
		"python": "python3",
		"pip": "python3 -m pip",
		"ls": "ls",
		"clear": "clear"
	}
	
	OPTIONS = {
		"win32": WIN_COMMANDS,
		"other": UNIX_COMMANDS
	}

	try:
		return OPTIONS[sys.platform][command.lower()] if sys.platform == "win32" else OPTIONS["other"][command.lower()]
	except:
		return command


BOLD = "\033[1m"
FAIL = "\033[91m"
WARNING = "\033[93m"
WHITE = "\33[97m"
RESET = "\033[0m"
AQUA = "\033[96m"
BLUE = "\033[34m"
GREEN = "\033[92m"
SCHEME = {
	"display": WHITE,
	"error": FAIL,
	"warning": WARNING
}

def format_(content: str, type_: str):
	return content.replace(
		"%bold%",
		BOLD
	).replace(
		"%red%",
		FAIL
	).replace(
		"%yellow%",
		WARNING
	).replace(
		"%aqua%",
		AQUA
	).replace(
		"%blue%",
		BLUE
	).replace(
		"%green%",
		GREEN
	).replace(
		"%white%",
		WHITE
	).replace(
		"%r%",
		SCHEME.get(type_)
	)

class Terminal:
	format = "%d-%m-%Y | %H:%M:%S"
	log = False
	log_file = None
	error_func = None

	@staticmethod
	def apply_format(content: str, type_: str):
		return format_(content, type_)

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
	def display(content: str):
		time = datetime.now()
		if Terminal.log is True:
			file = open(f"{Terminal.log_file}.log", "a")
			file.write(time.strftime(f"[{Terminal.format}] INFO: ") + f"{content}" + "\n")
			content = format_(content, "display")
		print(BOLD + WHITE + time.strftime(f"[{Terminal.format}] INFO: ") + RESET + WHITE + f"{content}" + RESET)

	@staticmethod
	def warn(content: str):
		time = datetime.now()
		if Terminal.log is True:
			file = open(f"{Terminal.log_file}.log", "a")
			file.write(time.strftime(f"[{Terminal.format}] WARNING: ") + f"{content}" + "\n")
			content = format_(content, "warning")
		print(BOLD + WARNING + time.strftime(f"[{Terminal.format}] WARNING: ") + RESET + WARNING + f"{content}" + RESET)

	@staticmethod
	def error(content: str):
		time = datetime.now()
		if Terminal.log is True:
			file = open(f"{Terminal.log_file}.log", "a")
			file.write(time.strftime(f"[{Terminal.format}] ERROR: ") + f"{content}" + "\n")
			content = format_(content, "error")
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

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

from typing import TypeVar, Any
import json

MISSING = 0.0

__all__ = (
	'JSON'
)

T = TypeVar('T', bound='JSON')


class JSON:
	def __init__(self):
		self.file = None

	def open(file: str) -> None:
		if file.endswith(".json"):
			file = file[:-5]
		JSON.file = file
		return None

	def get_data(variable) -> Any:
		file = JSON.file
		if file == None:
			raise RuntimeError("File not opened with JSON.open()")

		try:
			with open(f"{file}.json", "r") as jsonFile:
				data = json.load(jsonFile)
			return data[variable]
		except:
			return None

	def register_value(variable, value) -> None:
		file = JSON.file
		if file == None:
			raise RuntimeError("File not opened with JSON.open()")

		try:
			with open(f"{file}.json", "r") as jsonFile:
				data = json.load(jsonFile)
		
			data[variable] = value
		
			with open(f"{file}.json", "w") as jsonFile:
				json.dump(data, jsonFile)
		
		except:
			data = {}
			data[variable] = value
		
			with open(f"{file}.json", "w") as jsonFile:
				json.dump(data, jsonFile)

	def format(json: dict, indent: int=2, *args) -> dict:
		return json.dumps(json, indent=indent, *args)

	def build(*args) -> dict:
		data = {}
		count = 1
		_count = 0
		for i in range(len(list(args))):
			if count > len(list(args)):
				break
			try:
				data.update({args[_count]: args[count]})
			except:
				return data
			count += 2
			_count += 2
		return data
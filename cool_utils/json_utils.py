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

from typing import TypeVar
import itertools
import json

MISSING = 0.0

__all__ = (
	'JSON'
)

T = TypeVar('T', bound='JSON')


class JSON:
	def __init__(self):
		self.file = None

	def open(self, file: str):
		self.file = file

	def get_data(self, variable: str):
		file = self.file
		if file == None:
			raise RuntimeError("File not opened with JSON.open()")

		try:
			with open(f"{file}.json", "r") as jsonFile:
				data = json.load(jsonFile)
			return data[variable]
		except:
			return None

	def register_value(self, variable: str, value):
		file = self.file
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

	def format(self, json: dict, indent: int=2):
		return json.dumps(json, indent=indent)

	def build_json(self, *args):
		data = {}
		count = 1
		_count = 0
		for i in range(len(list(args))):
			data.update({args[_count]: args[count]})
			count += 1
			_count, count += 1
		return data
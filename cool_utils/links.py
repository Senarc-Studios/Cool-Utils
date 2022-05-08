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

import re
import string

from typing import TypeVar

from ._missing import MISSING

REGEX = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,4}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"

__all__ = (
	'Links'
)

T = TypeVar('T', bound='Links')


def get_slash():
	slash = "\ "
	slash = slash.replace(" ", "")
	return slash


class Links:
	def __init__(self, whitelist: list = []):
		self.whitelist = whitelist

	@classmethod
	def check(self, content: str) -> bool:
		word_list = []
		ascii_chars = list(string.ascii_uppercase + string.ascii_lowercase + "0123456789.")

		for character in content:
			if character not in ascii_chars:
				content = content.replace(character, " ")
		for word in content.split(" "):
			word_list.append(word)
		_count = -1
		for word in word_list:
			_count += 1
			if word == ".":
				return True
			if re.match(REGEX, word) and word not in self.whitelist:
				return True
			else:
				return False

	@classmethod
	def censor(self, content: str, censor: str = "*", strict: bool = True) -> str:
		word_list = []
		if strict:
			_processed_words = []
			ascii_chars = list(string.ascii_uppercase + string.ascii_lowercase + "0123456789.")

			count = 0
			_string = ""

			for character in content:
				if character not in ascii_chars:
					content = content.replace(character, " ")
			for word in content.split(" "):
				word_list.append(word)
			_count = -1
			for word in word_list:
				_count += 1
				if word == ".":
					try:
						_processed_words[_count - 1] = "".join([censor for i in range(len(word_list[_count - 1]))])
						_processed_words[_count] = censor
						_processed_words[_count + 1] = "".join([censor for i in range(len(word_list[_count + 1]))])
						count += 1
						continue
					except IndexError:
						break
				if re.match(REGEX, word) and word not in self.whitelist:
					count += 1
					word = "".join([censor for i in range(len(word))])
				_processed_words.append(word)
				_string = _string + word + " "

			if count == 0:
				return content

			else:
				final_string = ""
				for string_ in _processed_words:
					final_string += string_ + " "
				return final_string

		else:
			character_list = [';', get_slash(), '|', '-', '"', '&', '$', '@', '+', '^', '_', '<', '[', '!', '=', '>', '(',
		                  ')', '}', "'", '`', ']', '#', '%', '?', '*', '{', ',', '~']

			count = 0
			_string = ""

			for character in character_list:
				text = content.replace(character, " ")
			for word in text.split(" "):
				word_list.append(word)
			for word in word_list:
				if re.match(REGEX, word) and word not in self.whitelist:
					count += 1
					word = "".join([censor for i in range(len(word))])

				_string = _string + word + " "

			if count == 0:
				return content

			else:
				return _string

	@classmethod
	def find(self, content: str) -> list:
		word_list = []
		ascii_chars = list(string.ascii_uppercase + string.ascii_lowercase + "0123456789.")

		link_list = []
		for character in content:
			if character not in ascii_chars:
				content = content.replace(character, " ")
		for word in content.split(" "):
			if word != "":
				word_list.append(word)
		count = -1
		for word in word_list:
			count += 1
			if word == ".":
				word = word_list[count - 1] + word + word_list[count + 1]
			if re.match(REGEX, word) and word not in self.whitelist:
				link_list.append(word)
			else:
				continue

		return link_list

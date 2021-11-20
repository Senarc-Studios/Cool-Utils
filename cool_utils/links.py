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
from typing import TypeVar

REGEX = "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,4}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
MISSING = 0.0

__all__ = (
	'Links'
)

T = TypeVar('T', bound='Links')

def get_slash():
	slash = "\ "
	slash = slash.replace(" ", "")
	return slash

class Links:
	def check(content: str) -> bool:
		word_list = []
		character_list = [';', get_slash(), '|', '-', '"', '&', '$', '@', '+', '^', '_', '<', '[', '!', '=', '>', '(', ')', '}', "'", '`', ']', '#', '%', '?', '*', '{', ',', '~']

		for character in character_list:
			text = content.replace(character, " ")
		for word in text.split(" "):
			word_list.append(word)
		for word in word_list:
			if re.match(REGEX, word):
				return True
			else:
				return False

	def censor(content: str, censor: str = "*") -> str:
		word_list = []
		character_list = [';', get_slash(), '|', '-', '"', '&', '$', '@', '+', '^', '_', '<', '[', '!', '=', '>', '(', ')', '}', "'", '`', ']', '#', '%', '?', '*', '{', ',', '~']

		count = 0
		string = ""

		for character in character_list:
			text = content.replace(character, " ")
		for word in text.split(" "):
			word_list.append(word)
		for word in word_list:
			if re.match(REGEX, word):
				count = count + 1
				word = "".join([censor for i in range(len(word))])

			string = string + word + " "

		if count == 0:
			return content

		else:
			return string

	def find(content: str) -> list:
		word_list = []
		character_list = [';', get_slash(), '|', '-', '"', '&', '$', '@', '+', '^', '_', '<', '[', '!', '=', '>', '(', ')', '}', "'", '`', ']', '#', '%', '?', '*', '{', ',', '~']

		link_list = []

		for character in character_list:
			text = content.replace(character, " ")
		for word in text.split(" "):
			word_list.append(word)
		for word in word_list:
			if re.match(REGEX, word):
				link_list.append(word)
			else:
				continue

		return link_list
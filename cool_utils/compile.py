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

import itertools
from typing import TypeVar

from ._missing import MISSING

__all__ = (
	'Compile'
)

T = TypeVar('T', bound='Compile')


def check_type(list, item_type):
	for item in list:
		if isinstance(item, item_type):
			continue
		else:
			raise TypeError(f"Only {item_type} is supported for this function.")


class Compile:
	@staticmethod
	def all_possible_cases(
			text: str
	):
		results = []
		for x in itertools.product(*zip(text.upper(), text.lower())):
			first = "".join(x)
			results.append(first)
		return results

	@staticmethod
	def string(
			string_list: list,
			joints: str = MISSING,
			startswith: str = MISSING,
			endswith: str = MISSING
	):
		if not isinstance(string_list, list):
			raise TypeError(f"Only Lists are supported to be compiled.")
		check_type(string_list, str)
		compiled_string = ""
		if startswith is not None:
			compiled_string = startswith + compiled_string

		compiled_string = joints.joint(string_list)

		if endswith is not None:
			compiled_string = compiled_string + endswith

		return compiled_string

	@staticmethod
	def to_string(
			item_list: list,
			joints: str = MISSING,
			startswith: str = MISSING,
			endswith: str = MISSING
	):
		if not isinstance(item_list, list):
			raise TypeError(f"Only Lists are supported to be compiled.")
		compiled_string = ""
		if startswith is not None:
			compiled_string = startswith + compiled_string

		compiled_string = joints.joint(item_list)

		if endswith is not None:
			compiled_string = compiled_string + endswith

		return compiled_string

	@staticmethod
	def numbers(
			number_list,
			joints: int = MISSING,
			startswith: int = MISSING,
			endswith: int = MISSING
	):
		if not isinstance(number_list, list):
			raise TypeError(f"Only Lists are supported to be compiled.")
		check_type(number_list, int)
		compiled_string = ""
		if startswith is not None:
			compiled_string = f"{startswith}"

		compiled_string = joints.joint(number_list)

		if endswith is not None:
			compiled_string = compiled_string + f"{endswith}"

		return int(compiled_string)

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

from typing import TypeVar, Any, Optional, overload

from ._missing import MISSING

_cache = {
	"_size": 0,  # linter = bad
}

__all__ = (
	'Cache'
)

T = TypeVar('T', bound='Cache')


class GlobalCache:
	@staticmethod
	def store(variable: str, value: Any) -> None:
		if variable == "_size":
			raise ValueError("Cannot store _size")

		payload = {
			"_size": (1 + _cache["_size"]),
			f"{variable}": value
		}
		_cache.update(payload)
		return None

	@staticmethod
	@overload
	def load(variable: str) -> Any:
		...

	@staticmethod
	@overload
	def load(variable: str, default: Optional[Any] = MISSING) -> Any:
		...

	@staticmethod
	def load(variable: Optional[Any] = MISSING, default: Optional[Any] = MISSING) -> Any:
		if variable is MISSING:
			c = _cache.copy()
			del c["_size"]
			return c

		if variable == "_size":
			raise ValueError("Cannot load _size")

		try:
			return _cache[variable]
		except KeyError:
			if default is MISSING:
				raise

			return default

	@staticmethod
	def size() -> int:
		return _cache["_size"]

	@staticmethod
	def clear() -> None:
		key_list = []
		for key, value in _cache.items():
			if key == "_size":
				continue
			key_list.append(key)

		for key in key_list:
			del _cache[key]

		default_payload = {
			"_size": 0
		}

		_cache.update(default_payload)

	@staticmethod
	def remove(variable: Any) -> Any:
		if variable == "_size":
			raise ValueError("Cannot remove _size")

		return _cache.pop(variable)


class Cache:
	def __init__(self):
		self._cache = {"_size": 0}

	def store(self, variable: str, value: Any) -> None:
		if variable == "_size":
			raise ValueError("Cannot store _size")

		payload = {
			"_size": (1 + self._cache["_size"]),
			f"{variable}": value
		}
		self._cache.update(payload)
		return None

	@overload
	def load(self, variable: str) -> Any:
		...

	@overload
	def load(self, variable: str, default: Optional[Any] = MISSING) -> Any:
		...

	def load(self, variable: Optional[Any] = MISSING, default: Optional[Any] = MISSING) -> Any:
		if variable is MISSING:
			c = self._cache.copy()
			del c["_size"]
			return c

		if variable == "_size":
			raise ValueError("Cannot load _size")

		try:
			return self._cache[variable]
		except KeyError:
			if default is MISSING:
				raise

			return default

	def size(self) -> int:
		return self._cache["_size"]

	def clear(self) -> None:
		key_list = []
		for key, value in self._cache.items():
			if key == "_size":
				continue
			key_list.append(key)

		for key in key_list:
			del self._cache[key]

		default_payload = {
			"_size": 0
		}

		self._cache.update(default_payload)

	def remove(self, variable: Any) -> Any:
		if variable == "_size":
			raise ValueError("Cannot remove _size")

		return self._cache.pop(variable)

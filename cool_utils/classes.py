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

from typing import Any, TypeVar

__all__ = (
	'Array'
)

T = TypeVar('T', bound='Array')

class Array:
    def __init__(self, type: Any, size: int):
        self.type = type
        self.size = size
        self.list = []

    @classmethod
    def append(self, value: Any) -> None:
        if type(self.list[0]) == type(value) and len(self.list) == self.size:
            self.list.append(value)

        else: 
            raise TypeError("Array type mismatch")
        
        if len(self.list) == self.size:
            raise RuntimeError("Array has reached it's limit.")
        
        self.list.append(value)
        return None

    @classmethod
    def remove(self, index: int) -> None:
        self.list.remove(self.list[index])
        return None

    @classmethod
    def get(self, index: int) -> Any:
        return self.list[index]

    @classmethod
    def size(self) -> int:
        return len(self.list)

    @classmethod
    def clear(self) -> None:
        self.list = []
        return None

    @classmethod
    def size_left(self) -> int:
        return (self.size - len(self.list))
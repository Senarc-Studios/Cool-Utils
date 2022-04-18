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

import json
from typing import TypeVar, Any, Optional, Union, overload

from ._missing import MISSING

__all__ = (
    'JSON'
)

T = TypeVar('T', bound='JSON')
G = TypeVar('G', bound='GlobalJSON')

class JSON:
    def __init__(self, file: str, *, indent: Optional[Union[int, str]] = None) -> None:
        self.file = file
        self.indent = indent

    @classmethod
    def open(cls, file: str) -> T:
        if file.endswith(".json"):
            file = file[:-5]

        return cls(file)

    @staticmethod
    def format(data: Any, indent: int = 2, **kwargs) -> str:
        return json.dumps(data, indent=indent, **kwargs)

    @staticmethod
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

    def _check_file(self) -> str:
        file = self.file
        if file is None:
            raise RuntimeError("File not opened with JSON.open()")

        return file

    def load(self) -> Any:
        file = self._check_file()

        try:
            with open(f"{file}.json", "r") as jsonFile:
                return json.load(jsonFile)
        except:
            return None

    @overload
    def write(self, data: Any, **kwargs) -> None:
        ...

    @overload
    def write(self, data: Any, indent: Optional[Union[int, str]], **kwargs) -> None:
        ...

    def write(self, data: Any, indent: int = MISSING, **kwargs) -> None:
        file = self._check_file()

        if indent is MISSING:
            indent = self.indent

        try:
            with open(f"{file}.json", "w") as jsonFile:
                json.dump(data, jsonFile, indent=indent, **kwargs)
        except:
            return

    def get_data(self, variable) -> Any:
        file = self._check_file()

        try:
            data = self.load()
            return data[variable]
        except:
            return None

    def register_value(self, variable, value) -> None:
        file = self._check_file()

        try:
            data = self.load()

            data[variable] = value

            self.write(data)
        except:
            data = {}
            data[variable] = value

            with open(f"{file}.json", "w") as jsonFile:
                json.dump(data, jsonFile)


class GlobalJSON:
    file: str = None
    indent: Optional[Union[int, str]] = None

    @staticmethod
    def open(file: str) -> None:
        if file.endswith(".json"):
            file = file[:-5]

        GlobalJSON.file = file

    @staticmethod
    def format(data: Any, indent: int = 2, **kwargs) -> str:
        return json.dumps(data, indent=indent, **kwargs)

    @staticmethod
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

    @staticmethod
    def load() -> Any:
        file = GlobalJSON.file
        if file is None:
            raise RuntimeError("File not opened with JSON.open()")

        try:
            with open(f"{file}.json", "r") as jsonFile:
                return json.load(jsonFile)
        except:
            return None

    @staticmethod
    @overload
    def write(data: Any, **kwargs) -> None:
        ...

    @staticmethod
    @overload
    def write(data: Any, indent: Optional[Union[int, str]] = MISSING, **kwargs) -> None:
        ...

    @staticmethod
    def write(data: Any, indent: int = MISSING, **kwargs) -> None:
        file = GlobalJSON.file
        if file is None:
            raise RuntimeError("File not opened with JSON.open()")

        if indent is MISSING:
            indent = GlobalJSON.indent

        try:
            with open(f"{file}.json", "w") as jsonFile:
                json.dump(data, jsonFile, indent=indent, **kwargs)
        except:
            return

    @staticmethod
    def get_data(self, variable) -> Any:
        file = GlobalJSON.file
        if file is None:
            raise RuntimeError("File not opened with JSON.open()")

        try:
            data = self.load()
            return data[variable]
        except:
            return None

    @staticmethod
    def register_value(self, variable, value) -> None:
        file = GlobalJSON.file
        if file is None:
            raise RuntimeError("File not opened with JSON.open()")

        try:
            data = self.load()

            data[variable] = value

            self.write(data)
        except:
            data = {}
            data[variable] = value

            with open(f"{file}.json", "w") as jsonFile:
                json.dump(data, jsonFile)

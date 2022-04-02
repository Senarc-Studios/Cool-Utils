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
import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from typing import TypeVar

__all__ = (
	'Mongo'
)

T = TypeVar('T', bound='Mongo')


class Mongo:
	def __init__(self, mongo_url, database):
		cluster = AsyncIOMotorClient(mongo_url)
		cluster.get_io_loop = asyncio.get_running_loop
		self.client = cluster
		self.db = self.client[database]

	@classmethod
	async def collection(self, name: str):
		return self.db[name]

	@classmethod
	async def insert(self, collection, data):
		return await collection.insert_one(data)

	@classmethod
	def find(self, collection, query):
		return collection.find(query)

	@classmethod
	async def find_one(self, collection, query):
		return await collection.find_one(query)

	@classmethod
	async def update(self, collection, query, data):
		return await collection.update_one(query, data)

	@classmethod
	async def delete(self, collection, query):
		return await collection.delete_one(query)

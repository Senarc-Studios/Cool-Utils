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

from motor.motor_asyncio import AsyncIOMotorClient
from typing import TypeVar
import itertools

MISSING = 0.0

__all__ = (
	'Mongo'
)

T = TypeVar('T', bound='Mongo')


class Mongo:
	def __init__(self):
		self.null = None
		self.client = None
		self.db = None
		self.collection = None

	def connect(mongo_url, database):
	 Mongo.client = AsyncIOMotorClient(mongo_url)
	 Mongo.db = Mongo.client[database]

	def set_collection(collection):
	 Mongo.collection = Mongo.db[collection]

	async def insert(data):
		if Mongo.collection == None:
			raise RuntimeError("Collection not set")
		return await Mongo.collection.insert_one(data)

	def find(query):
		if Mongo.collection == None:
			raise RuntimeError("Collection not set")
		return Mongo.collection.find(query)

	async def find_one(query):
		if Mongo.collection == None:
			raise RuntimeError("Collection not set")
		return await Mongo.collection.find_one(query)

	async def update(query, data):
		if Mongo.collection == None:
			raise RuntimeError("Collection not set")
		await Mongo.collection.update_one(query, data)

	async def delete(query):
		if Mongo.collection == None:
			raise RuntimeError("Collection not set")
		await Mongo.collection.delete_one(query)

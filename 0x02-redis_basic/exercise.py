#!/usr/bin/env python3
""" Writing strings to Redis """
from uuid import uuid4
from typing import Union, Callable, Optional
import redis

UnionOfTypes = Union[str, bytes, int, float]

class Cache:
    """ Class for methods that operate a caching system """

    def __init__(self):
        """ Instance of the Redis db """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """
        Method that returns a string
        """
        self._key = str(uuid4())
        self._redis.set(self._key, data)
        return self._key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> UnionOfTypes:
        """
        Retrieves data stored in redis using a key and
        converts result back to desired format
        """
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, value: str) -> str:
        """ get string """
        return self.get(self._key, str)

    def get_int(self, value: str) -> int:
        """ get int """
        return self.get(self._key, int)

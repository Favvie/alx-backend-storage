#!/usr/bin/env python3
"""writing strings to redis"""

import redis
import uuid
from typing import Callable, Union


class Cache:
    def __init__(self):
        """initialization function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store a key"""
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable):
        value = self._redis.get(key)
        fn(value)

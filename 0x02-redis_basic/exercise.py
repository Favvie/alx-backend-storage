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
        if key is None:
            return None
        try:
            if fn is not None:
                value = fn(value)
        except Exception:
            return None
        return value

    def get_str(self, key: str) -> str:
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        return self.get(key, lambda x: int(x))

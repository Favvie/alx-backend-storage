#!/usr/bin/env python3
"""writing strings to redis"""

import redis
import uuid


class Cache:
    def __init__(self):
        """initialization function"""
        self._redis = redis.Redis()

    def store(self, data: str | bytes | int | float) -> str:
        """"""
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

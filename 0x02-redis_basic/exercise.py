#!/usr/bin/env python3
"""writing strings to redis"""

import redis
import uuid
from typing import Callable, Union, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count call decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """a wrapper function"""
        key = method.__qualname__
        count = self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """call history decorator"""
    inputKey = f"{method.__qualname__}:inputs"
    outputKey = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ a wrrapper function"""
        self._redis.rpush(inputKey, str(args))
        output = method(self, *args, *kwargs)
        self._redis.rpush(outputKey, str(output))
        return output
    return wrapper


def replay(method):
    """get the history of a function"""
    name = method.__qualname__
    cache = redis.Redis()
    try:
        count = int(cache.get(name).decode('utf-8'))
    except Exception:
        c = 0
    print(f"{name} ws called {count} times:")
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)

    for key, value in zip(inputs, outputs):
        try:
            key = key.decode('utf-8')
        except Exception:
            key = ''
        try:
            value = value.decode('utf-8')
        except Exception:
            value = ''
        print(f"{name}(*{key.decode('utf-8')}) -> {value.decode('utf-8')}")


class Cache:
    def __init__(self):
        """initialization function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store a key"""
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """get the value of a key"""
        value = self._redis.get(key)
        if key is not None and fn is not None and callable(fn):
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """parametrize Cache.get for string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """parametrize Cache.get for int value"""
        value = self.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value

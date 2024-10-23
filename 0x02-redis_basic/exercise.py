#!/usr/bin/python3

""""Module for redis exercise store an instance of the Redis client as a private variable named
_redis (using redis.Redis()) and flush the instance using flushdb."""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

class Cache:
    """Class for redis exercise store an instance of the Redis client as a private variable named
_redis (using redis.Redis()) and flush the instance using flushdb."""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
    def store (self, data: Union[str, bytes, int, float]) -> str:
        """Method that takes a data argument and returns a string."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
if __name__ == "__main__":
    cache = Cache()
    print(cache.store("Hello hbtn!"))
    
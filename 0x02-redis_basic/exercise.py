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
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Method that takes a key string argument and an optional Callable argument named fn.
        This callable will be used to convert the data back to the desired format."""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data
    def get_int(self, key: str) -> int:
        """Method that takes a key string argument and returns an integer."""
        data = self._redis.get(key)
        return int(data)
    def get_str(self, key: str) -> str:
        """Method that takes a key string argument and returns a string."""
        data = self._redis.get(key)
        return str(data)
if __name__ == "__main__":
    cache = Cache()
    print(cache.store("Hello World"))
    print(cache.store(1024))
    print(cache.store(3.14))
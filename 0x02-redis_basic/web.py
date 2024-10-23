#!/usr/bin/env python3
"""Module for caching and tracking URL access with Redis."""

import redis
import requests
from functools import wraps
from typing import Callable


# Connect to Redis
r = redis.Redis()


def cache_with_tracker(expiration: int = 10) -> Callable:
    """Decorator for caching and tracking URL access.

    Args:
        expiration (int): Time in seconds for cache expiration. Defaults to 10.

    Returns:
        Callable: Decorated function with caching and tracking.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            """Wrapper function that implements caching and tracking.

            Args:
                url (str): URL to fetch and cache.

            Returns:
                str: HTML content of the URL.
            """
            cache_key = f"cached:{url}"
            count_key = f"count:{url}"

            # Track access count
            r.incr(count_key)

            # Check if cached result exists
            cached_result = r.get(cache_key)
            if cached_result:
                return cached_result.decode('utf-8')

            # Fetch and cache the result if not in cache
            result = func(url)
            r.setex(cache_key, expiration, result)
            return result
        return wrapper
    return decorator


@cache_with_tracker(expiration=10)
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL.

    Args:
        url (str): URL to fetch.

    Returns:
        str: HTML content of the URL.
    """
    response = requests.get(url)
    return response.text

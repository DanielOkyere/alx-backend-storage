#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
from typing import Union, Optional, Callable
from uuid import uuid4


class Cache:
    """ Class Cache """
    def __init__(self) -> None:
        """ Initializes redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores data in redis chache
        Args:
            data (dict): data to store
        Returns:
            str: key
        """
        k = str(uuid4())
        self._redis.set(k, data)
        return k

    def get(self, key: str, fn: Optional[Callable] = None)\
            ->  Union[str, bytes, int, float, None]:
        """ Fetch data from redis cache """
        data = self._redis.get(key)
        if data is not None and fn is not None and Callable(fn):
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Get data as string from cache
        Args:
            key (str): key
        Returns:
            str: data
        """
        d = self.get(key, lambda x: x.decode('utf-8'))
        return d

    def get_int(self, key: str) -> Union[str, bytes, int, float]:
        """
        Get data as integer from redis
        Args:
            key (str): key
        Returns:
            int: data
        """
        return self.get(key, int)

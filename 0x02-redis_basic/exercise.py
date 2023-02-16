#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
from typing import Union
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

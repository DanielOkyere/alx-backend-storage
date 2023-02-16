#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps


def replay(func: Callable) -> None:
    """ definition for history """
    r = redis.Redis()
    key = func.__qualname__
    inp = r.lrange("{}:inputs".format(key), 0, -1)
    outp = r.lrange("{}:outputs".format(key), 0, -1)
    if len(inp) == 1:
        print("{} was called {} {}:".format(key, len(inp), 'time'))
    else:
        print("{} was called {} {}:".format(key, len(inp), 'times'))

    for k, v in zip(inp, outp):
        print("{}(*{}) -> {}".format(key,
                                     k.decode('utf-8'),
                                     v.decode('utf-8')
                                    ))


def call_history(method: Callable) -> Callable:
    """ decorator to store history of inputs and outputs of a particular
    function"""
    @wraps(method)
    def call_history_wr(self, *args, **kwargs):
        """ definition of callhistory wrapper"""
        key = method.__qualname__
        inp_m = key + ":inputs"
        outp_m = key + ":outputs"
        self._redis.rpush(inp_m, str(args))
        fin = method(self, *args, **kwargs)
        self._redis.rpush(outp_m, str(fin))
        return fin
    return call_history_wr


def count_calls(method: Callable) -> Callable:
    """ decorator to wrap count """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ definition of wrapper """
        key = method.__qualname__
        self._redis.incr(key, 1)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Class Cache """
    def __init__(self) -> None:
        """ Initializes redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
            -> Union[str, bytes, int, float, None]:
        """ Fetch data from redis cache """
        data = self._redis.get(key)
        return data if not fn else fn(data)

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

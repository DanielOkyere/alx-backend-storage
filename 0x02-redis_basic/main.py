#!/usr/bin/env python3
import redis
Cache = __import__('exercise').Cache

cache = Cache()

cache.store("foo")
cache.store("bar")
cache.store(42)
print(replay(cache.store))

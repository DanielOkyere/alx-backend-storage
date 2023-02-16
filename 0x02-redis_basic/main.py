#!/usr/bin/env python3
import redis
Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inp = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inp))
print("outputs: {}".format(outs))

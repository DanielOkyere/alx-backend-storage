#!/usr/bin/env python3
import redis
Cache = __import__('exercise').Cache

cache = Cache()
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}
for v, fn in TEST_CASES.items():
    key = cache.store(v)
    assert cache.get(key, fn=fn) == v

local_redis = redis.Redis()
print(local_redis.get(key))

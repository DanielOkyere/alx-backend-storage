#!/usr/bin/env python3
""" Implementing an expiring web cache tracker """
import requests
import time
from functools import wraps
from typing import Dict

cache: Dict[str, str] = {}

def get_page(url: str) -> str:
    if url in cache:
        print(f"Retrieving from cache: {url}")
        return cache[url]
    else:
        print(f"Retrieving from web: {url}")
        res = requests.get(url)
        result = res.text
        cache[url] = result
        return result

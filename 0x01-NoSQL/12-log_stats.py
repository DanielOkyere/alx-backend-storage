#!/usr/bin/env python3
""" 12 Log stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(log_collection.count_documents({})))
    print("Methods:")
    for m in methods:
        print("\tmethod {}: {}".format(m, log_collection.count_documents({
            "method": m
        })))
    print("{} status check".format(log_collection.count_documents({
        "path": "/status"
    })))

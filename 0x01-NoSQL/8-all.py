#!/usr/bin/env python3
"""
Python Script to query all collection from mongo db
"""


def list_all(mongo_collection):
    """
    list_all - lists all documents in a mongo_collection
    Args:
        mongo_collection (mongo object)
    Returns:
        List of all documents in the collection
    """
    return mongo_collection.find()

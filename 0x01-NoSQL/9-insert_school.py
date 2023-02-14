#!/usr/bin/env python3
"""
Script to insert new document in a collection based
on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert_school - inserts many schools
    Args:
        mongo_collection (mongo object)
        kwargs key word arguments
    Returns:
        _id new id of last school created
    """
    return mongo_collection.insert_one(kwargs).inserted_id

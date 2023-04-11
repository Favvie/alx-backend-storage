#!/usr/bin/env python3
"""insert a document using pymongo"""


def insert_school(mongo_collection, **kwargs):
    """insert a doc into a collection called school"""
    data = {}
    for key, value in kwargs.items():
        data[key] = value
    id = mongo_collection.insert_one(data).inserted_id
    return id

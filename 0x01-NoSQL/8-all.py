#!/usr/bin/env python3
"""using pymongo"""


def list_all(mongo_collection):
    """list all documents"""
    listDocs = list(mongo_collection.find())
    if len(listDocs) == 0:
        return []
    return mongo_collection.find()

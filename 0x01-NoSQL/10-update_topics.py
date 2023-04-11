#!/usr/bin/env python3
"""Write a Python func that changes all topics of a doc based on the name"""


def update_topics(mongo_collection, name, topics):
    """update a doc"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

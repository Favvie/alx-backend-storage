#!/usr/bin/env python3
"""Write a Python func that changes all topics of a doc based on the name"""


def update_topics(mongo_collection, name, topics):
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})

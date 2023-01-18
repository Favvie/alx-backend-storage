#!/usr/bin/env python3
<<<<<<< HEAD
"""
change school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update many rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
=======
""" 10-update_topics.py """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name """
    if mongo_collection is not None:
        return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
>>>>>>> cf076995d6a71022a7a491972e849f4434e79222

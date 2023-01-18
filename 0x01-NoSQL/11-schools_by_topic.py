#!/usr/bin/env python3
<<<<<<< HEAD
"""
find by topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Find by topic
    """
    return mongo_collection.find({"topics": topic})
=======
""" 11-schools_by_topic.py """


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    if mongo_collection is not None:
        return mongo_collection.find({"topics": topic})
>>>>>>> cf076995d6a71022a7a491972e849f4434e79222

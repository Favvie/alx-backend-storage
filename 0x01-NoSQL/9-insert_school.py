#!/usr/bin/env python3
<<<<<<< HEAD
"""
This module have a utility function that insert documents
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert into school
    """
    return mongo_collection.insert_one(kwargs).inserted_id
=======
""" 9-insert_school.py """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """
    if mongo_collection is not None:
        return mongo_collection.insert_one(kwargs).inserted_id
>>>>>>> cf076995d6a71022a7a491972e849f4434e79222

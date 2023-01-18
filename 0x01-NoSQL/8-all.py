#!/usr/bin/env python3
<<<<<<< HEAD
"""
This module have a utility function that list all document
"""
import pymongo


def list_all(mongo_collection):
    """
    list all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
=======
""" 8-all.py """


def list_all(mongo_collection):
    """ lists all documents in a collection """
    if mongo_collection is not None:
        return mongo_collection.find()
>>>>>>> cf076995d6a71022a7a491972e849f4434e79222

#!/usr/bin/env python3
<<<<<<< HEAD
"""
students
"""


def top_students(mongo_collection):
    """ students by score """
=======
"""14. Top students"""


def top_students(mongo_collection):
    """Python function that returns all
    students sorted by average score:
    mongo_collection will be the pymongo collection object
    The top must be ordered
    The average score must be part of each item returns with
    key = averageScore"""

>>>>>>> cf076995d6a71022a7a491972e849f4434e79222
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
<<<<<<< HEAD
                    "averageScore": {"$avg": "$topics.score"}
=======
                    "averageScore": {
                        "$avg": "$topics.score"
                    }
>>>>>>> cf076995d6a71022a7a491972e849f4434e79222
                }
        },
        {
            "$sort":
<<<<<<< HEAD
                {
                    "averageScore": -1
                }
=======
            {
                "averageScore": -1
            }
>>>>>>> cf076995d6a71022a7a491972e849f4434e79222
        }
    ])

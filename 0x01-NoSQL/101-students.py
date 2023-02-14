#!/usr/bin/env python3
""" 101-students.py """


def top_students(mongo_collection):
    """ Aggregate top students """
    return mongo_collection.aggregate([
        {
            "$project":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ])

#!/usr/bin/env python3
''' module for task 10 '''


def update_topics(mongo_collection, name, topics):
    ''' function that changes all topics of a school document'''
    mongo_collection.update_many({"name": name}, {"$set": {'topics': topics}})

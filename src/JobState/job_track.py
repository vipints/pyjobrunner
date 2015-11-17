#!/usr/bin/env python
"""

"""

# common packages
import datetime

#import custom packages
import mongo


def job_logs(arg_tuple):
    """
    """

    mongo_table = mongo.MongoTable("x230", "pygrid" ,"job_state")

    result = {}
    
    result["id"] = None
    result["timestamp"] = datetime.datetime.now()

    mongo_table.save(result)



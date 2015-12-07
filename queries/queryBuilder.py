# Filename: queryBuilder.py
# Author: Osei Seraphin
# Course: IST 440w
# Instructor: Professor Oakes

from pymongo import MongoClient
from ConstantValues.Constants import constantsclass


class queryBuilder:

    client = MongoClient('localhost', 27017)
    db = client.eia_data
    weeklyCollections = constantsclass.WEEKLY_COLLECTIONS
    monthlyCollections = constantsclass.MONTHLY_COLLECTIONS
    yearlyCollections = constantsclass.YEARLY_COLLECTIONS
    PredictionTypes = constantsclass.PREDICTION_TYPES

    def retrieveCollection(self, region, predictionType):

        # Pulls the correct Mongo collection name based on prediction type and region
        if predictionType.upper() == queryBuilder.PredictionTypes[2]:
            region = queryBuilder.weeklyCollections[region.upper()]

        elif predictionType.upper() == queryBuilder.PredictionTypes[1]:
            region = queryBuilder.monthlyCollections[region.upper()]

        else:
            region = queryBuilder.yearlyCollections[region.upper()]

        collection = queryBuilder.db[region]

        data = collection.find({},{"_id":0})

        return data

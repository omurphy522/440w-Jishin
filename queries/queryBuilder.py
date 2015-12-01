__author__ = 'Osei'

import pymongo
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
            region = queryBuilder.weeklyCollections[region]

        elif predictionType.upper() == queryBuilder.PredictionTypes[1]:
            region = queryBuilder.monthlyCollections[region]

        else:
            region = queryBuilder.yearlyCollections[region]

        collection = queryBuilder.db[region]

        data = collection.find()

        return data

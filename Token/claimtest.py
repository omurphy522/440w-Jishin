import jwt
import sys
sys.path.append('..')
from pymongo import MongoClient

username = 'oween'
 #Declare client and database being used
client = MongoClient()
db = client.eia_data
collection = db.users
databasePayload = collection.distinct("claims" , {'username': username})
print databasePayload
#tokenPayload = ""
for claims  in databasePayload:
    for claim in claims:
        print claim
                        #tokenPayload+=claims[claim]
#jsonPayload = loads(tokenPayload)
           # jsonPayload = loads(claimList)
#print jsonPayload


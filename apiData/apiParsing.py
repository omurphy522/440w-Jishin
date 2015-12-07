# Name: apiParsing
# Author(s): Brian Gracin, Owen Murphy
# Course: IST 440W
# Professor: Senior Lecturer Joseph Oakes
# Created: 11/2/2015
# Modified: 11/18/2015


from pymongo import MongoClient
import urllib2
from xml.etree import ElementTree as ET

try:
    import apiList
except ImportError as e:
    print "Import local file apiList not found"

import sys
sys.path.append('..')
from jishinLogger import LoggingFinal as jishinLogging



class APIParse:
    def apiCollectionFreshPull(self):
        try:
            # Declare client and database being used
            client = MongoClient()
            db = client.eia_data
            # Purge database collections
            db.dropDatabase()
        except Exception as dbE:
            jishinLogging.logger.error("Mongo error ", dbE)

        try:
            # Populate requestURLs object with api urls from file
            requestURLs = apiList.getApiUrls()
        except Exception as apiE:
            jishinLogging.logger.error("Method not found: ", apiE)

        try:
            # Iterate through list of URLs
            for apiUrl in requestURLs:

                # Parse the current api file
                dataRow = APIParse.parseAPI(self, apiUrl)

                # Pull name for collection stored in requestURLs object
                collection = db[apiUrl['name']]

                # Iterate through XML members to populate documents
                for row in dataRow:
                    date = row.find('date').text
                    value = row.find('value').text
                    post = {"date": date, "value": value}
                    collection.insert_one(post)
        except urllib2.HTTPError:
            jishinLogging.logger.error("Could not download file ", apiUrl['url'])
        except Exception as e:
            jishinLogging.logger.error("Exception: ", e)

    def apiCollectionUpdate(self):
        try:
            # Declare client and database being used
            client = MongoClient()
            db = client.eia_data
        except Exception as dbE:
            jishinLogging.logger.error("Mongo error: ", dbE)

        try:
            # Populate requestURLs object with api urls from file
            requestURLs = apiList.getApiUrls()
        except Exception as apiE:
            jishinLogging.logger.error("Method not found: ", apiE)

        try:
            # Iterate through list of URLs
            for apiUrl in requestURLs:

                # Parse the current api file
                dataRow = APIParse.parseAPI(self, apiUrl)

                # Pull name for collection stored in requestURLs object
                collection = db[apiUrl['name']]

                # Grab date from most recent data point for comparison
                if collection.count() != 0:
                    last_data_set = max(collection.find({}, {"date": 1, "_id": 0}))

                # Iterate through XML members to populate documents
                for row in dataRow:
                    date = row.find('date').text

                    if date > last_data_set['date']:
                        value = row.find('value').text
                        post = {"date": date, "value": value}
                        collection.insert_one(post)

                        return True
        except urllib2.HTTPError:
            jishinLogging.logger.error("Could not download file ", apiUrl['url'])
        except Exception as e:
            jishinLogging.logger.error("Exception: ", e)

    def parseAPI(self, apiUrl):

        dataRow = ""

        try:
            # Request XML object from API
            tree = ET.parse(urllib2.urlopen(apiUrl['url']))

            # Parse XML, code would have to change if XML format changes
            series = tree.find("series")
            seriesRow = series.find("row")
            data = seriesRow.find("data")
            dataRow = data.findall("row")

        except Exception as e:
            jishinLogging.logger.error("Exception: " , e)

        return dataRow
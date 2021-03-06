# Name: apiParsing
# Author(s): Brian Gracin, Owen Murphy
# Course: IST 440W
# Professor: Senior Lecturer Joseph Oakes
# Created: 11/2/2015
# Modified: 12/05/2015


from pymongo import MongoClient
import urllib2
from xml.etree import ElementTree as ET

try:
    import apiList
except ImportError as e:
    print "Import local file apiList not found"

import sys
sys.path.append('..')
from mikeLogging import LoggingFinal as jishinLogging



class APIParse:
    def apiCollectionFreshPull(self):

        jishinLogging.logger.info("API Fresh Pull started")

        try:
            # Declare client and database being used
            client = MongoClient()
            db = client.eia_data
            # Purge database collections
            db.dropDatabase()
        except Exception as dbE:
            jishinLogging.logger.error("Mongo error: %s" % dbE)

        try:
            # Populate requestURLs object with api urls from file
            requestURLs = apiList.getApiUrls()
        except Exception as apiE:
            jishinLogging.logger.error("Method not found: %s" % apiE)

        try:
            # Iterate through list of URLs
            for apiUrl in requestURLs:

                # Parse the current api file
                dataRow = self.parseAPI(apiUrl)

                # Pull name for collection stored in requestURLs object
                collection = db[apiUrl['name']]

                # Iterate through XML members to populate documents
                for row in dataRow:
                    date = row.find('date').text
                    value = row.find('value').text
                    post = {"date": date, "value": value}
                    collection.insert_one(post)

            jishinLogging.logger.info("API Fresh Pull completed")

        except urllib2.HTTPError:
            jishinLogging.logger.error("Could not download file ", apiUrl['url'])
        except Exception as e:
            jishinLogging.logger.error("Exception: %s" % e)

    def apiCollectionUpdate(self):

        jishinLogging.logger.info("API Update started")

        try:
            # Declare client and database being used
            client = MongoClient()
            db = client.eia_data
        except Exception as dbE:
            jishinLogging.logger.error("Mongo error: %s" % dbE)

        try:
            # Populate requestURLs object with api urls from file
            requestURLs = apiList.getApiUrls()
        except Exception as apiE:
            jishinLogging.logger.error("Method not found: %s" % apiE)

        try:
            # Iterate through list of URLs
            for apiUrl in requestURLs:

                # Parse the current api file
                dataRow = self.parseAPI(apiUrl)

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

            jishinLogging.logger.info("API Update completed")

        except urllib2.HTTPError:
            jishinLogging.logger.error("Could not download file %s" % apiUrl['url'])
        except Exception as e:
            jishinLogging.logger.error("Exception: %s" % e)

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
            jishinLogging.logger.error("Exception: %s" % e)

        return dataRow
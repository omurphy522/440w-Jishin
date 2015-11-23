#Name: apiParsing
#Author(s): Brian Gracin, Owen Murphy
#Course: IST 440W
#Professor: Senior Lecturer Joseph Oakes
#Created: 11/2/2015
#Modified: 11/16/2015

try:
    from pymongo import MongoClient
except ImportError as e:
    print "Import MongoClient not found"
try:
    import urllib2
except ImportError as e:
    print "Import urllib2 not found"
try:
    import apiList
except ImportError as e:
    print "Import local file apiList not found"
try:
    from xml.etree import ElementTree as ET
except ImportError as e:
    print "Import ElementTree not found"


try:
    #Declare client and database being used
    client = MongoClient()
    db = client.eia_data
    #Purge database collections
    db.dropDatabase()
except Exception as e:
    print "Mongo error ", e

try:
    #Populate requestURLs object with api urls from file
    requestURLs = apiList.getApiUrls()
except Exception:
    print "Method not found"

try:
    #Iterate through list of URLs
    for apiUrl in requestURLs:
        #Request XML object from API
        tree = ET.parse(urllib2.urlopen(apiUrl['url']))

        #Parse XML, code would haveto change if XML format changes
        root = tree.getroot()
        series = tree.find("series")
        seriesRow = series.find("row")
        data = seriesRow.find("data")
        dataRow = data.findall("row")

        #Pull name for collection stored in requestURLs object
        collection = db[apiUrl['name']]

        #Iterate through XML members to populate documents
        for row in dataRow:
            date = row.find('date').text
            value = row.find('value').text
            post = {"date": date, "value": value}
            collection.insert_one(post)
except urllib2.HTTPError:
    print "Could not download file ", apiUrl['url']
except Exception as e:
    print "Exception ", e

#Updates collections if api contains data points newer than latest in database
from pymongo import MongoClient
import urllib2
import api_list
from xml.etree import ElementTree as ET

client = MongoClient()
db = client.eia_data

requestURLs = api_list.get_api_urls()

for api_url in requestURLs:
    tree = ET.parse(urllib2.urlopen(api_url['url']))
    root = tree.getroot()
    
    series = tree.find("series")
    series_row = series.find("row")

    data = series_row.find("data")
    data_row = data.findall("row")

    collection = db[api_url['name']]
    last_data_set = max(collection.find({},{"date":1, "_id":0}))

    for row in data_row:
        date = row.find('date').text
        
        if date > last_data_set['date']:
            value = row.find('value').text        
            post = {"date": date, "value": value}
            collection.insert_one(post)

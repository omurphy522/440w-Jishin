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
    row = series.find("row")
    data = row.find("data")
    row2 = data.findall("row")
    collection = db[api_url['name']]
    for row in row2:
        date = row.find('date').text
        value = row.find('value').text
        post = {"date": date, "value": value}
        collection.insert_one(post)

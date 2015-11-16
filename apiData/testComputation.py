#Name: testComputations
#Author(s): Brian Gracin
#Course: IST 440W
#Professor: Senior Lecturer Joseph Oakes
#Created: 10/19/2015
#Modified: 11/2/2015

try:
    from pymongo import MongoClient
except ImportError as e:
    print "Import MongoClient not found"
from time import mktime
from datetime import date
from datetime import timedelta
import math
import time

collection_name = raw_input("Enter collection name: ")

try:
    #Declare client and database being used
    client = MongoClient()
    db = client.eia_data
    collection = db[collection_name]
except Exception as e:
    print "Mongo error ", e

data_set = collection.find({},{"_id":0})
date_list = []
value_list = []
date_squared_list = []
date_value_list = []

try:
    #Weekly
    for data in data_set:
       #Get date stored in document
       raw_date = data['date']

       #Split and remake string so that it can be parsed
       string_date = raw_date[:4] + ' ' + raw_date[4:6] + ' ' + raw_date[6:]

       #Parse string into struct_time format
       struct_date = time.strptime(string_date, "%Y %m %d")

       #Convert struct_time into date format
       date_date = date.fromtimestamp(mktime(struct_date))

       #Convert date to ordinal format and normalize for computation
       ordinal_date = date_date.toordinal() - 727657 #4/4/1993

       #Populate lists to be used for computation
       date_list.append(ordinal_date)
       date_squared_list.append(pow(float(ordinal_date), 2))
       value_list.append(float(data['value']))
       date_value_list.append(ordinal_date * float(data['value']))
except Exception as e:
    print "Error in Weekly data parsing: ", e

#Monthly
#for data in data_set:
#   raw_date = date['date']
#
#   string_date = raw_date[:4] + ' ' + raw_date[4:]
#   struct_date = time.strptime(string_date, "%Y %m")
#   date_date = date.fromtimestamp(mktime(struct_date))
#   date_date + timedelta(days=15)
#   ordinal_date = date_date.toordinal - 727667

#Yearly
#for data in data_set:
#   raw_date = date['date']
#
#   struct_date = time.strptime(raw_date, "%Y")
#   date_date = date.fromtimestamp(mktime(struct_date))
#   date_date + timedelta(days=182)
#   ordinal_date = date_date.toordinal()

try:
    #Basic computation to be revised
    date_average = sum(date_list) / float(len(date_list))
    value_average = sum(value_list) / float(len(value_list))
    date_value_average = sum(date_value_list) / float(len(date_value_list))
    date_squared_averge = sum(date_squared_list) / float(len(date_squared_list))

    slope = ((date_average * value_average) - date_value_average) / (pow(date_average, 2) - date_squared_averge)

    b = value_average - (slope * date_average)
except TypeError:
    print "Invalid value"

try:
    user_input = raw_input("Enter integer: ")

    outcome = (slope * int(user_input)) + b
except TypeError:
    print "Invalid value in user input or outcome"

print(outcome)

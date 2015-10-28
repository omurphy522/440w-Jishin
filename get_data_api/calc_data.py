from pymongo import MongoClient
from datetime import datetime
from time import mktime
from datetime import date
import math
import time

client = MongoClient()
db = client.eia_data

collection = db.us_all_w

data_set = collection.find({},{"_id":0})
date_list = []
value_list = []
date_squared_list = []
date_value_list = []

for data in data_set:
   raw_date = data['date']

   string_date = raw_date[:4] + ' ' + raw_date[4:6] + ' ' + raw_date[6:]
   struct_date = time.strptime(string_date, "%Y %m %d")
   date_date = date.fromtimestamp(mktime(struct_date))
   ordinal_date = date_date.toordinal() - 727657

   date_list.append(ordinal_date)
   date_squared_list.append(pow(float(ordinal_date), 2))
   value_list.append(float(data['value']))
   date_value_list.append(ordinal_date * float(data['value']))

date_average = sum(date_list) / float(len(date_list))
value_average = sum(value_list) / float(len(value_list))
date_value_average = sum(date_value_list) / float(len(date_value_list))
date_squared_averge = sum(date_squared_list) / float(len(date_squared_list))

slope = ((date_average * value_average) - date_value_average) / (pow(date_average, 2) - date_squared_averge)

b = value_average - (slope * date_average)

user_input = raw_input("Enter integer: ")

outcome = (slope * int(user_input)) + b

print(outcome)

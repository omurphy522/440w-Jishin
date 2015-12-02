# Name: testComputations
# Author(s): Brian Gracin
# Course: IST 440W
# Professor: Senior Lecturer Joseph Oakes
# Created: 10/19/2015
# Modified: 11/18/2015

import sys
sys.path.append('..')
from time import mktime
from datetime import date
from datetime import timedelta
import time

class ComputationClass:

    def computationalCalculations(self, data_set, interval, prediction_date):

        date_list = []
        value_list = []
        date_squared_list = []
        date_value_list = []
        date_to_check = 0

        try:
            for data in data_set:

                if interval == 'w':
                    # Weekly
                    ordinal_date = ComputationClass.weeklyDateConvert(self, data)

                elif interval == 'm':
                    # Monthly
                    ordinal_date = ComputationClass.monthlyDateConvert(self, data)

                elif interval == 'a':
                    # Yearly
                    ordinal_date = ComputationClass.yearlyDateConvert(self, data)

                date_to_check = ComputationClass.convertPredictionDate(prediction_date)

                # Populate lists to be used for computation
                date_list.append(ordinal_date)
                date_squared_list.append(pow(float(ordinal_date), 2))
                value_list.append(float(data['value']))
                date_value_list.append(ordinal_date * float(data['value']))
        except Exception as e:
            print "Error in Weekly data parsing: ", e

        # Run Linear Regression on data pulled
        compute_return = ComputationClass.linearRegression(self, date_list, value_list, date_value_list,
                                                           date_squared_list, date_to_check)

        return compute_return

    def linearRegression(self, date_list, value_list, date_value_list, date_squared_list, date_to_check):

        slope = ""
        b = ""

        try:
            # Basic computation to be revised
            date_average = sum(date_list) / float(len(date_list))
            value_average = sum(value_list) / float(len(value_list))
            date_value_average = sum(date_value_list) / float(len(date_value_list))
            date_squared_average = sum(date_squared_list) / float(len(date_squared_list))

            slope = ((date_average * value_average) - date_value_average) / (pow(date_average, 2) - date_squared_average)

            b = value_average - (slope * date_average)
        except TypeError:
            print "Invalid value"

        try:
            outcome = (slope * int(date_to_check)) + b
        except TypeError:
            print "Invalid value in user input or outcome"

        return outcome

    def weeklyDateConvert(self, data):
        try:
            # Get date stored in document
            raw_date = data['date']

            # Split and remake string so that it can be parsed
            string_date = raw_date[:4] + ' ' + raw_date[4:6] + ' ' + raw_date[6:]

            # Parse string into struct_time format
            struct_date = time.strptime(string_date, "%Y %m %d")

            # Convert struct_time into date format
            date_date = date.fromtimestamp(mktime(struct_date))

            # Convert date to ordinal format and normalize for computation
            ordinal_date = date_date.toordinal() - 727657  # 4/4/1993

            return ordinal_date
        except Exception as e:
            print "Error in Weekly date parsing: ", e

    def monthlyDateConvert(self, data):
        try:
            # Get date stored in document
            raw_date = data['date']

            # Split and remake string so that it can be parsed
            string_date = raw_date[:4] + ' ' + raw_date[4:]

            # Parse string into struct_time format
            struct_date = time.strptime(string_date, "%Y %m")

            # Convert struct_time into date format
            date_date = date.fromtimestamp(mktime(struct_date))

            # Correct for middle of the month
            date_date + timedelta(days=15)

            # Convert date to ordinal format and normalize for computation
            ordinal_date = date_date.toordinal() - 727667

            return ordinal_date
        except Exception as e:
            print "Error in Monthly date parsing: ", e

    def yearlyDateConvert(self, data):
        try:
            # Get date stored in document
            raw_date = data['date']

            # Parse string into struct_time format
            struct_date = time.strptime(raw_date, "%Y")

            # Convert struct_time into date format
            date_date = date.fromtimestamp(mktime(struct_date))

            # Correct for middle of the year
            date_date + timedelta(days=182)

            # Convert date to ordinal format and normalize for computation
            ordinal_date = date_date.toordinal() - 727564

            return ordinal_date
        except Exception as e:
            print "Error in Yearly date parsing: ", e

    def convertPredictionDate(self, prediction_date):

        ordinal_date = 0

        try:
            # Split and remake string so that it can be parsed
            string_date = prediction_date[:2] + ' ' + prediction_date[2:4] + ' ' + prediction_date[4:]

            # Parse string into struct_time format
            struct_date = time.strptime(string_date, "%m %d %Y")

            # Convert struct_time into date format
            date_date = date.fromtimestamp(mktime(struct_date))

            ordinal_date = date_date.toordinal() - 727657

        except Exception as e:
            print "Error converting prediction date: ", e

        return ordinal_date

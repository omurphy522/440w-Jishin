# Name: testComputations
# Author(s): Brian Gracin
# Course: IST 440W
# Professor: Senior Lecturer Joseph Oakes
# Created: 10/19/2015
# Modified: 12/03/2015

import sys

sys.path.append('..')
from time import mktime
from datetime import date
from datetime import timedelta
from jishinLogger import LoggingFinal as jishinLogging
import time


class ComputationClass:
    def linearRegression(self, date_list, value_list, date_value_list, date_squared_list, date_to_check):

        outcome = 0

        try:
            # Basic computation to be revised
            date_average = sum(date_list) / float(len(date_list))
            value_average = sum(value_list) / float(len(value_list))
            date_value_average = sum(date_value_list) / float(len(date_value_list))
            date_squared_average = sum(date_squared_list) / float(len(date_squared_list))

            slope = ((date_average * value_average) - date_value_average) / (
            pow(date_average, 2) - date_squared_average)

            b = value_average - (slope * date_average)

            outcome = (slope * int(date_to_check)) + b

        except TypeError as e:
            jishinLogging.logger.error("Invalid value: %s" % e)

        return outcome

    def weeklyDateConvert(self, data):

        ordinal_date = 0

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

        except Exception as e:
            jishinLogging.logger.error("Error in Weekly date parsing: %s " % e)

        return ordinal_date

    def monthlyDateConvert(self, data):

        ordinal_date = 0

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

        except Exception as e:
            jishinLogging.logger.error("Error in Monthly date parsing: %s " % e)

        return ordinal_date

    def yearlyDateConvert(self, data):

        ordinal_date = 0

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

        except Exception as e:
            jishinLogging.logger.error("Error in Yearly date parsing: %s " % e)

        return ordinal_date

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
            jishinLogging.logger.error("Error converting prediction date: %s" % e)

        return ordinal_date

    def computationalCalculations(self, data_set, interval, prediction_date):

        date_list = []
        value_list = []
        date_squared_list = []
        date_value_list = []
        date_to_check = 0

        try:
            for item in data_set:
                if interval == 'WEEKLY':
                    # Weekly
                    ordinal_date = self.weeklyDateConvert(item)

                elif interval == 'MONTHLY':
                    # Monthly
                    ordinal_date = self.monthlyDateConvert(item)

                elif interval == 'ANNUAL':
                    # Yearly
                    ordinal_date = self.yearlyDateConvert(item)

                # Populate lists to be used for computation
                date_list.append(ordinal_date)
                date_squared_list.append(pow(float(ordinal_date), 2))
                value_list.append(float(item['value']))
                date_value_list.append(ordinal_date * float(item['value']))

            date_to_check = self.convertPredictionDate(prediction_date)

        except Exception as e:
            jishinLogging.logger.error('Error in Weekly data parsing: %s ' % e)

        # Run Linear Regression on data pulled
        compute_return = self.linearRegression(date_list, value_list, date_value_list,
                                               date_squared_list, date_to_check)

        return compute_return

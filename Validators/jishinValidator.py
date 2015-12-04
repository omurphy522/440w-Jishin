# Filename: jishinValidator.py
# Author: Osei Seraphin
# Course: IST 440w
# Instructor: Professor Oakes

from Errors import InputErrors
from Errors import ValidationErrors
import re

SpecialCharacters = re.compile(r'[<>/{}[\]~`]')
Letters = re.compile(r'[a-zA-Z]')
ThirtyDays = ['04','06','09','11']
ThirtyOneDays = ['01','03','05','07','08','10','12']
Regions = ['US', 'EAST_COAST', 'NEW_ENGLAND', 'CENTRAL_ATLANTIC', 'LOWER_ATLANTIC', 'MIDWEST', 'GULF_COAST',
           'ROCK_MOUNTAINS', 'WEST_COAST']
PredictionTypes = ['ANNUAL', 'MONTHLY', 'WEEKLY']

class Input_Validator:
    def __init__(self):
        self.errors = []

    def has_error(self):
        return len(self.errors) > 0

    def reset_error(self):
        self.errors = []

    def add_error(self, e):
        self.reset_error()
        self.errors.append(e)

    def validate_date(self, currentdate, date):

        CurrentDay = int(currentdate.day)
        CurrentMonth = int(currentdate.month)
        CurrentYear = int(currentdate.year)

        if len(date) != 8:
            self.add_error(ValidationErrors.InputError(date, InputErrors.InputErrors.INCORRECT_DATE_LENGTH))
            raise ValidationErrors.InputError(date, InputErrors.InputErrors.INCORRECT_DATE_LENGTH)
        elif SpecialCharacters.search(date):
            self.add_error(ValidationErrors.InputError(date, InputErrors.InputErrors.DATE_CONTAINS_SPECIAL_CHARACTER))
            raise ValidationErrors.InputError(date, InputErrors.InputErrors.DATE_CONTAINS_SPECIAL_CHARACTER)
        elif Letters.search(date):
            self.add_error(ValidationErrors.InputError(date, InputErrors.InputErrors.DATE_CONTAINS_SPECIAL_CHARACTER))
            raise ValidationErrors.InputError(date, InputErrors.InputErrors.DATE_CONTAINS_LETTER)
        else:
            month = int(date[:2])
            day = int(date[2:4])
            year = int(date[4:])


            # Validates Year
            if year < CurrentYear:
                self.add_error(ValidationErrors.InputError(year, InputErrors.InputErrors.INCORRECT_YEAR_VALUE))
                raise ValidationErrors.InputError(year, InputErrors.InputErrors.INCORRECT_YEAR_VALUE)

            # Validates Month
            elif month > 12:
                self.add_error(ValidationErrors.InputError(month, InputErrors.InputErrors.INCORRECT_MONTH_VALUE))
                raise ValidationErrors.InputError(month, InputErrors.InputErrors.INCORRECT_MONTH_VALUE)
            elif year == CurrentYear and month <= CurrentMonth:
                self.add_error(ValidationErrors.InputError(month, InputErrors.InputErrors.INVALID_MONTH))
                raise ValidationErrors.InputError(month, InputErrors.InputErrors.INVALID_MONTH)

            # Validates Day

            elif str(month) in ThirtyDays and day > 30:
                self.add_error(ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH))
                raise ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH)
            elif str(month) in ThirtyOneDays and day > 31:
                self.add_error(ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH))
                raise ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH)
            elif year % 4 != 0 and month == 2 and day > 28:
                self.add_error(ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH))
                raise ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH)
            elif year % 4 == 0 and month == 2 and day > 29:
                self.add_error(ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH))
                raise ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH)
            elif year == CurrentYear and month == CurrentMonth and day <= CurrentDay:
                self.add_error(ValidationErrors.InputError(day, InputErrors.InputErrors.INCORRECT_DAY_VALUE))
                raise ValidationErrors.InputError(day, InputErrors.InputErrors.INCORRECT_DAY_VALUE)

    def validate_region(self, region):
        if region.upper() not in Regions:
            self.add_error(ValidationErrors.InputError(region, InputErrors.InputErrors.INVALID_REGION))
            raise ValidationErrors.InputError(region, InputErrors.InputErrors.INVALID_REGION)

    def validate_prediction_type(self, predictionType):
        if predictionType.upper() not in PredictionTypes:
            self.add_error(ValidationErrors.InputError(predictionType, InputErrors.InputErrors.INVALID_PREDICTION_TYPE))
            raise ValidationErrors.InputError(predictionType, InputErrors.InputErrors.INVALID_PREDICTION_TYPE)

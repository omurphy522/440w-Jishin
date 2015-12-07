# Filename: validationTest.py
# Author: Osei Seraphin
# Course: IST 440w
# Instructor: Professor Oakes

import sys
sys.path.append('..')

import unittest
from Validators import jishinValidator
from Errors import ValidationErrors
from datetime import datetime


validator = jishinValidator.Input_Validator()
currentDate = datetime.strptime('02/27/2015', '%m/%d/%Y')

class validation_tests(unittest.TestCase):


####### Date Validation
    def test_validate_date_ok(self):

        date = '12312018'
        validator = jishinValidator.Input_Validator()

        validator.validate_date(currentDate, date)

        self.assertFalse(validator.has_error())


    def test_validate_date_incorrect_length(self):

        date = '112018'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_date, currentDate, date)

    def test_validate_date_contains_special_characters(self):

        date = '1231201]'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_date, currentDate, date)

    def test_validate_date_contains_letter(self):

        date = '1231201a'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_date, currentDate, date)

####### Year Validation
    def test_validate_date_incorrect_year(self):

        date = '12312014'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_date, currentDate, date)

####### Month Validation
    def test_validate_date_incorrect_month(self):

        date = '15312015'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_date, currentDate, date)

    def test_validate_date_invalid_month(self):

        date = '01312015'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_date, currentDate, date)

####### Day Validation
    def test_validate_date_invalid_day_for_month_with_thirty_days(self):

        date = '11312016'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_date, currentDate, date)

    def test_validate_date_invalid_day_for_month_with_thirty_one_days(self):

        date = '12322016'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_date, currentDate, date)

    def test_validate_date_valid_day_in_february(self):

        validator = jishinValidator.Input_Validator()
        date = '02292016'

        validator.validate_date(currentDate, date)

        self.assertFalse(validator.has_error())

    def test_validate_date_invalid_day_in_february(self):

        date = '02292017'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_date, currentDate, date)

    def test_validate_date_invalid_day_in_february_leap_year(self):

        date = '02302016'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_date, currentDate, date)

    def test_validate_date_invalid_day_in_month(self):

        date = '02262015'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_date, currentDate, date)

####### Region validation
    def test_validate_region_ok(self):

        region = 'us'
        validator = jishinValidator.Input_Validator()

        validator.validate_region(region)

        self.assertFalse(validator.has_error())

    def test_validate_region_invalid_region(self):

        region = 'catdog'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_region, region)

####### Prediction Type validation
    def test_validate_prediction_type_ok(self):

        predictionType = 'monthly'
        validator = jishinValidator.Input_Validator()

        validator.validate_prediction_type(predictionType)

        self.assertFalse(validator.has_error())

    def test_validate_prediction_type_invalid_prediction_type(self):

        predictionType = 'catdog'
        validator = jishinValidator.Input_Validator()

        self.assertRaises(ValidationErrors.InputError, validator.validate_prediction_type, predictionType)

if __name__ == '__main__':
    unittest.main()

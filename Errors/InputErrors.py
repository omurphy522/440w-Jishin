# Filename: inputErrors.py
# Author: Osei Seraphin
# Course: IST 440w
# Instructor: Professor Oakes

from enum import Enum


class InputErrors(Enum):

##### Date Errors
    INCORRECT_DATE_LENGTH = 'Please enter date in format: mmddyyyy'
    DATE_CONTAINS_LETTER = 'Date cannot contain any letters'
    DATE_CONTAINS_SPECIAL_CHARACTER = 'Date cannot contain any special characters'

##### Year Errors
    INCORRECT_YEAR_VALUE = 'Year must come after the current year'

##### Month Errors
    INCORRECT_MONTH_VALUE = 'Month must be between 01 and 12'
    INVALID_MONTH = 'Month cannot come before the current month'

##### Day Errors
    INCORRECT_DAY_VALUE = 'Day must be between 1 and 31.'
    INVALID_DAY_IN_MONTH = 'That day does not exist in the specified month.'

##### Region Errors
    INVALID_REGION = 'Please enter a valid region'

##### Prediction Type Errors
    INVALID_PREDICTION_TYPE = 'Please select whether you want an Annual, Monthly, or Weekly prediction'

##### RabbitMQ Error
    NO_TAG_ERROR = "No Delivery Tag"

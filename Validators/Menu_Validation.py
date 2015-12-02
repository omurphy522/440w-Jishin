from Errors import InputErrors
from Errors import ValidationErrors
import re
from datetime import datetime
from ConstantValues.Constants import constantsclass

SpecialCharacters = re.compile(r"[<>/{}[\]~`]")
Letters = re.compile(r"[a-zA-Z]")
ThirtyDays = ['04','06','09','11']
ThirtyOneDays = ['01','03','05','07','08','10','12']
CurrentYear = datetime.now().year
CurrentMonth = datetime.now().month
CurrentDay = datetime.now().day
Regions = ['US', 'EAST_COAST', 'NEW_ENGLAND', 'CENTRAL_ATLANTIC', 'LOWER_ATLANTIC', 'MIDWEST', 'GULF_COAST',
           'ROCK_MOUNTAINS', 'WEST_COAST']
PredictionTypes = constantsclass.PREDICTION_TYPES

class Input_Validator:

    def validate_date(self, date):

        if len(date) != 8:
            raise ValidationErrors.InputError(date, InputErrors.InputErrors.INCORRECT_DATE_LENGTH)
        elif SpecialCharacters.match(date):
            raise ValidationErrors.InputError(date, InputErrors.InputErrors.DATE_CONTAINS_SPECIAL_CHARACTER)
        elif Letters.match(date):
            raise ValidationErrors.InputError(date, InputErrors.InputErrors.DATE_CONTAINS_LETTER)
        else:
            month = date[:2]
            day = date[2:4]
            year = date[4:]

            # Validates Year
            if int(year) < int(CurrentYear):
                raise ValidationErrors.InputError(year, InputErrors.InputErrors.INCORRECT_YEAR_VALUE)

            # Validates Month
            elif int(month) > 12:
                raise ValidationErrors.InputError(month, InputErrors.InputErrors.INCORRECT_MONTH_VALUE)
            elif year == CurrentYear and int(month) <= CurrentMonth:
                raise ValidationErrors.InputError(month, InputErrors.InputErrors.INCORRECT_MONTH_VALUE)

            # Validates Day
            elif month in ThirtyDays and int(day) > 30:
                raise ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH)
            elif month in ThirtyOneDays and int(day) > 31:
                raise ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH)
            elif int(year) % 4 != 0 and int(month) == 2 and int(day) > 28:
                raise ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH)
            elif int(year) % 4 == 0 and int(month) == 2 and int(day) > 29:
                raise ValidationErrors.InputError(day, InputErrors.InputErrors.INVALID_DAY_IN_MONTH)
            elif year == CurrentYear and month == CurrentMonth and day <= CurrentDay:
                raise ValidationErrors.InputError(day, InputErrors.InputErrors.INCORRECT_DAY_VALUE)

    def validate_region(self, region):
        if region.upper() not in Regions:
            raise ValidationErrors.InputError(region, InputErrors.InputErrors.INVALID_REGION)

    def validate_prediction_type(self, predictionType):
        if predictionType.upper() not in PredictionTypes:
            raise ValidationErrors.InputError(predictionType, InputErrors.InputErrors.INVALID_PREDICTION_TYPE)
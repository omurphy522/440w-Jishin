from Errors import InputErrors
from Errors import ValidationErrors
import re
from datetime import datetime


SpecialCharacters = re.compile(r"[<>/{}[\]~`]")
Letters = re.compile(r"[a-zA-Z]")
CurrentYear = datetime.now().year
CurrentMonth = datetime.now().month
States = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'HI', 'ID',
          'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT',
          'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR',
          'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY']


class Input_Validator:


    def valildate_year(self, year):
        if year is None:
            raise ValidationErrors.InputError(year,InputErrors.InputErrors.YEAR_IS_BLANK)
        elif len(year) != 4:
            raise ValidationErrors.InputError(year, InputErrors.InputErrors.INCORRECT_YEAR_LENGTH)
        elif SpecialCharacters.match(year):
            raise ValidationErrors.InputError(year, InputErrors.InputErrors.YEAR_CONTAINS_SPECIAL_CHARACTERS)
        elif Letters.match(year):
            raise ValidationErrors.InputError(year, InputErrors.InputErrors.YEAR_CONTAINS_LETTER)
        elif int(year) < int(CurrentYear):
            raise ValidationErrors.InputError(year, InputErrors.InputErrors.INCORRECT_YEAR_VALUE)


    def validate_month(self, month, year):
        if month is None:
            raise ValidationErrors.InputError(month, InputErrors.InputErrors.MONTH_IS_BLANK)
        elif len(month) != 2:
            raise ValidationErrors.InputError(month, InputErrors.InputErrors.INCORRECT_MONTH_LENGTH)
        elif SpecialCharacters.match(month):
            raise ValidationErrors.InputError(month, InputErrors.InputErrors.MONTH_CONTAINS_SPECIAL_CHARACTERS)
        elif Letters.match(month):
            raise ValidationErrors.InputError(month, InputErrors.InputErrors.MONTH_CONTAINS_LETTER)
        elif int(month) > 13:
            raise ValidationErrors.InputError(month, InputErrors.InputErrors.INCORRECT_MONTH_VALUE)
        elif year == CurrentYear and int(month) <= CurrentMonth:
            raise ValidationErrors.InputError(month, InputErrors.InputErrors.INCORRECT_MONTH_VALUE)

    def validate_state(self, state):

        if state is None:
            raise ValidationErrors.InputError(state, InputErrors.InputErrors.STATE_IS_BLANK)
        elif len(state) != 2:
            raise ValidationErrors.InputError(state, InputErrors.InputErrors.INCORRECT_STATE_FORMAT)
        elif SpecialCharacters.match(state):
            raise ValidationErrors.InputError(state, InputErrors.InputErrors.STATE_CONTAINS_SPECIAL_CHARACTERS)
        elif state not in States:
            raise ValidationErrors.InputError(state, InputErrors.InputErrors.INCORRECT_STATE_VALUE)

from enum import Enum

class InputErrors(Enum):
    # Year Errors
    INCORRECT_YEAR_LENGTH = 'Year must be a 4 digit value'
    INCORRECT_YEAR_VALUE = 'Year must come after the current year'
    YEAR_CONTAINS_LETTER = 'Year cannot contain any letters'
    YEAR_CONTAINS_SPECIAL_CHARACTERS = 'Year cannot contain any special characters'
    YEAR_IS_BLANK = 'Year cannot be left blank'

    # Month Errors
    INCORRECT_MONTH_LENGTH = 'Month must be a 2 digit value'
    INCORRECT_MONTH_VALUE = 'Month must be between 01 and 12'
    MONTH_CONTAINS_LETTER = 'Month cannot contain any letters'
    MONTH_CONTAINS_SPECIAL_CHARACTERS = 'Month cannot contain any special characters'
    MONTH_IS_BLANK = 'Month cannot be left blank'

    # State Errors
    INCORRECT_STATE_FORMAT = 'State ust be in the format of PA, NY, CA ...etc.'
    INCORRECT_STATE_VALUE = 'State must be one of the 50 states'
    STATE_CONTAINS_NUMBER = 'State cannot contain any numbers'
    STATE_CONTAINS_SPECIAL_CHARACTERS = 'State cannot contain any special characters'
    STATE_IS_BLANK = 'State cannot be left blank'


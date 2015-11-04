from validators import validationMenu
from errors import validationErrors
import sys
sys.path.append('..')



validator = validationMenu.Input_Validator()


menu = {}
menu['1'] = 'View average price in United States for a specific year.'
menu['2'] = 'View average price in United States for a specific month.'
menu['3'] = 'View average price in a State for a specific year.'
menu['4'] = 'View average price in a State for a specific month.'
menu['5'] = 'Exit'

while True:
    options = menu.keys()
    options.sort()

    for entry in options:
        print entry, menu[entry]
    selection = raw_input("Please choose an option: ")
    try:
        if selection == '1':

            print("You have selected:  %s" % (menu[selection]))

            year = raw_input("Enter the year would you like to predict prices for: ")
            validator.valildate_year(year)

            #     code for avg us gas price prediction in specified year

        elif selection == '2':

            print("You have selected:  %s" % (menu[selection]))

            year = raw_input("Enter the year would you like to predict prices for: ")
            validator.valildate_year(year)

            month = raw_input("Enter the month would you like to predict prices for: ")
            validator.validate_month(month, year)

            #     code for avg us gas price prediction in specified month

        elif selection == '3':

            print("You have selected:  %s" % (menu[selection]))

            year = raw_input("Enter the year would you like to predict prices for: ")
            validator.valildate_year(year)

            state = raw_input("Enter the state would you like to predict prices for: ").upper()
            validator.validate_state(state)
            #     code for avg state gas price prediction in specified year

        elif selection == '4':

            print("You have selected:  %s" % (menu[selection]))

            year = raw_input("Enter the year would you like to predict prices for: ")
            validator.valildate_year(year)

            month = raw_input("Enter the month would you like to predict prices for: ")
            validator.validate_month(month, year)

            state = raw_input("Enter the state would you like to predict prices for: ").upper()
            validator.validate_state(state)

            # code for avg state gas price prediction in specified month
            # prediction = predict_method(year, month, state)
            # print prediction
        elif selection == '5':

            print ("Goodbye")

        else:
            print "UNKNOWN SELECTION"
    except validationErrors.InputError as Err:
        print "ERROR: " + str(Err.msg)

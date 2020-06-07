import sys
from flight_trip import *
from passenger import *

user_input = input("Please enter password to begin or press 'x' to quit: ")
while user_input != 'x':
    if user_input == 'lovelyjubbly':
        class RunFile:
            new_flight = FlightTrip(destination='Rome', origin='Geneva', duration='1:00')
            new_passenger = Passenger(name='', passport_number='')
            user_input_a = input("press any key to continue or 'x' to abort: ")
            while user_input_a != 'x':
                user_input_1 = input("enter name or press 'x' to complete list: ")
                if user_input_1 == 'x':
                    sys.exit('Thank you, have a nice day')
                user_input_2 = int(input('enter passport number: '))
                new_passenger.create_name(user_input_1)
                new_passenger.set_passport_number(user_input_2)
                print(new_passenger.get_name(), new_passenger.get_passport_number())
                new_flight.add_passenger_details(user_input_1, user_input_2)
                new_flight.get_passenger_details()
                new_flight.create_passenger_dictionary()
                new_flight.get_passenger_dict()
                print(new_flight.get_passenger_dict())

            if user_input_a == 'x':
                sys.exit('Thank you, have a nice day')
    else:
        user_input = input("That is the wrong password, please try again or press 'x' to quit: ")
        if user_input == 'x':
            sys.exit('Thank you, have a nice day')




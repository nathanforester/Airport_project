import sys
from flight_trip import *
from passenger import *
from staff import *
from tickets import *

new_staff = Staff(f_name='', l_name='', password='')
user_input = input("Please enter name to begin or press 'x' to quit: ")
user_input_z = input('Please enter your last name: ')
new_staff.create_name(user_input, user_input_z)
while user_input != 'x':
    user_input_b = input("enter a new password or press 'x' to quit: ")
    if user_input_b == 'x':
        sys.exit('Thank you, have a nice day')
    new_staff.create_password(user_input_b)
    new_staff.get_password()
    user_input_c = input("Please re-enter your password: ")
    count = 3
    while user_input_c != user_input_b:
        count -= 1
        user_input_c = input("That is the wrong password, please try again or press 'x' to quit: ")
        while count < 0:
            sys.exit('bye')
        if user_input_c == 'x':
            sys.exit('Thank you, have a nice day')
    if user_input_c == user_input_b:
        print("login successful")
        user_input_a = input("press any key to continue or 'x' to abort: ")
        while user_input_a != 'x':
            new_flight = FlightTrip(flight_number='', destination='Rome', origin='Geneva', duration='1:00')
            user_input_Ive_lost_count = input("enter aircraft number: ")
            new_aircraft = Aircraft(aircraft_number='')
            new_aircraft.create_aircraft_number(user_input_Ive_lost_count)
            print(new_flight.create_flight_number(new_aircraft.get_aircraft_number()))
            new_ticket = Tickets(aircraft_number='', age='', ticket_price='', available_tickets=int())
            new_passenger = Passenger(f_name='', l_name='', passport_number='')
            user_input_part4 = int(input("enter age: "))
            new_ticket.ticket_cost(user_input_part4)
            print(new_ticket.get_ticket_price())
            new_ticket.decrement(user_input_part4)
            print(new_ticket.get_available())
            user_input_1 = input("enter name or press 'x' to complete list: ")
            if user_input_1 == 'x':
                sys.exit('Thank you, have a nice day')
            user_input_1a = input("enter last name: ")
            user_input_2 = int(input('enter passport number: '))
            new_passenger.create_name(user_input_1, user_input_1a)
            new_passenger.set_passport_number(user_input_2)
            print(new_passenger.get_f_name(), new_passenger.get_l_name(), new_passenger.get_passport_number())
            new_flight.add_passenger_details(new_passenger.create_name(user_input_1, user_input_1a), user_input_2)
            new_flight.get_passenger_details()
            dictionary = dict(zip(new_flight.passport_number_list, new_flight.passenger_list))
            print(dictionary)
        if user_input_a == 'x':
            sys.exit('Thank you, have a nice day')
        if user_input == 'x':
            sys.exit('Thank you, have a nice day')




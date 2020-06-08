from aircraft import *


class FlightTrip(Aircraft):

    def __init__(self, aircraft_number, destination, origin, duration, passenger_list=None, passport_number_list=None,
                 passenger_dict=None):
        super().__init__(self, aircraft_number)
        self.destination = destination
        self.origin = origin
        self.duration = duration
        if passenger_list is None:
            passenger_list = []
        self.passenger_list = passenger_list
        if passport_number_list is None:
            passport_number_list = []
        self.passport_number_list = passport_number_list
        if passenger_dict is None:
            passenger_dict = {}
        self.passenger_dict = passenger_dict

# create a flight trip with a specific destination
    def flight_destination(self):
        return self.destination
    # enter the flight destination and store it

    def flight_origin(self):
        return self.origin
# need to link the origin with destination
    # enter the origin of the flight (and link it to the destination)
# need to store the duration

    def duration(self):
        return self.duration
    # enter flight duration, store it
# need to create a passenger list

    def get_passenger_details(self):
        return self.passenger_list, self.passport_number_list

    def add_passenger_details(self, new_passenger, new_passport_number):
        self.passenger_list.append(str(new_passenger))
        self.passport_number_list.append(int(new_passport_number))
        return self.passenger_list, self.passport_number_list

    def get_passenger_dict(self):
        return self.passenger_dict

    def create_passenger_dictionary(self):
        keys = self.passport_number_list
        values = self.passenger_list
        self.passenger_dict = {key: [] for key in set(keys)}
        for a, b in zip(keys, values):
            self.passenger_dict[a].append(str(b))
        return str(self.passenger_dict)

    def return_string_list(self):
        return ''.join(self.create_passenger_dictionary())






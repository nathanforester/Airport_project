
class Aircraft:

    def __init__(self, aircraft_number, capacity):
        self.__aircraft_number = aircraft_number
        self.capacity = capacity

    def get_aircraft_number(self):
        return self.__aircraft_number

    def create_aircraft_number(self, new_aircraft_number):
        self.__aircraft_number = new_aircraft_number
        return new_aircraft_number

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, new_capacity):
        self.capacity = new_capacity
        # if passenger DOB > 2 years,decrement available seats
        return new_capacity
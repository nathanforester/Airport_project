from people import *


class Passenger(People):

    def __init__(self, name, passport_number):
        super().__init__(name=name, tax_number=None)
        self.__name = str(name)
        self.__passport_number = passport_number

    def get_passport_number(self):
        return self.__passport_number

    def set_passport_number(self, new_passport_number):
        self.__passport_number = new_passport_number
        return new_passport_number




from people import *


class Passenger(People):

    def __init__(self, f_name, l_name, passport_number):
        super().__init__(f_name=f_name, l_name=l_name, tax_number=None)
        self.__f_name = f_name
        self.__l_name = l_name
        self.__passport_number = passport_number

    def get_passport_number(self):
        return self.__passport_number

    def set_passport_number(self, new_passport_number):
        self.__passport_number = new_passport_number
        return new_passport_number




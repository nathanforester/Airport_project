
class Passenger:

    def __init__(self, name, passport_number):
        self.__name = str(name)
        self.__passport_number = passport_number

    def get_name(self):
        return self.__name

    def create_name(self, new_name):
        self.__name = new_name
        return new_name

    def get_passport_number(self):
        return self.__passport_number

    def set_passport_number(self, new_passport_number):
        self.__passport_number = new_passport_number
        return new_passport_number




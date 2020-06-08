from people import *


class Staff(People):

    def __init__(self, f_name, l_name, password):
        super().__init__(f_name=f_name, l_name=l_name, tax_number='')
        self.__password = password

    def get_password(self):
        return self.__password

    def create_password(self, new_password):
        self.__password = new_password
        return new_password

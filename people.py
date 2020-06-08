
class People:

    def __init__(self, name, tax_number):
        self.__name = name
        self.__tax_number = tax_number

    def get_name(self):
        return self.__name

    def create_name(self, new_name):
        self.__name = new_name
        return new_name

    def get_tax_number(self):
        return self.__tax_number

    def create_tax_number(self, new_tax_number):
        self.__tax_number = new_tax_number
        return new_tax_number


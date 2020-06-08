
class People:

    def __init__(self, f_name, l_name, tax_number):
        self.__f_name = f_name
        self.__l_name = l_name
        self.__tax_number = tax_number

    def get_f_name(self):
        return self.__f_name

    def get_l_name(self):
        return self.__l_name

    def create_name(self, f_new_name, l_new_name):
        self.__f_name = f_new_name
        self.__l_name = l_new_name
        new_name = f_new_name, l_new_name
        return ' '.join(new_name)

    def get_tax_number(self):
        return self.__tax_number

    def create_tax_number(self, new_tax_number):
        self.__tax_number = new_tax_number
        return new_tax_number


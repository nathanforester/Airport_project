from aircraft import *


class Tickets(Aircraft):

    def __init__(self, aircraft_number, capacity, age, ticket_price, available_tickets):  # discount):
        super().__init__(aircraft_number, capacity, age)
        self.age = age
        self.ticket_price = ticket_price
        self.available_tickets = available_tickets

    def get_available(self):
        return self.available_tickets

    def set_available(self, new_available):
        self.available_tickets = new_available
        return new_available

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age
        return new_age

    def get_ticket_price(self):
        return self.ticket_price

    def ticket_cost(self, new_age):
        if new_age < 2:
            self.ticket_price = 0
        if 2 < new_age < 13:
            self.ticket_price = 10
        else:
            self.ticket_price = 20
            return self.ticket_price

    def decrement(self, new_age):
        if new_age <= 0:
            return 'tickets sold out'
        while new_age > 2:
            self.capacity -= 1
            new_available = self.capacity
            return new_available














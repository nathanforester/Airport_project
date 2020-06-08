from aircraft import *


class Tickets(Aircraft):

    def __init__(self, aircraft_number, age, ticket_price, available_tickets):  # discount):
        super().__init__(aircraft_number)
        self.age = age
        self.ticket_price = ticket_price
        self.available_tickets = available_tickets

    def get_available(self):
        return self.available_tickets


    def get_dob(self):
        return self.age

    def get_ticket_price(self):
        return self.ticket_price

    def ticket_cost(self, new_age):
        if new_age < 2:
            self.ticket_price = 0
        elif 2 < new_age < 13:
            self.ticket_price = 10
        else:
            self.ticket_price = 20
        return self.ticket_price

    def decrement(self, new_age):
        self.available_tickets = 5
        for self.available_tickets in range(0, 5):
            if new_age > 2:
                self.available_tickets -= 1
            if self.available_tickets <= 0:
                return 'Sorry, no seats available. Hard cheese'
            return self.available_tickets
        else:
            return self.available_tickets







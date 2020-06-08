from aircraft import *


class Tickets(Aircraft):

    def __init__(self, aircraft_number, flight_number, available_tickets, ticket_price, discount):
        super().__init__(aircraft_number)
        self.flight_number = flight_number
        self.available_tickets = available_tickets
        self.ticket_price = ticket_price
        self.__discount = discount

    # get flight number

    # set and decrement/increment available tickets

    # calculate ticket price

    # apply discount
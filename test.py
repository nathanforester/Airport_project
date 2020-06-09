available_tickets = 5


def decrement(new_age):
    if available_tickets <= 0:
        return 'tickets sold out'
    while new_age > 2:
        return available_tickets - 1

    print(decrement(new_age=12))

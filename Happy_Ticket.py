# happy_ticket


def happy_ticket(a):
    ticket = [int(i) for i in a]
    len_ticket = len(ticket)//2
    return sum(ticket[:len_ticket]) == sum(ticket[len_ticket:])


ticket = input('Номер билета?')
print(happy_ticket(ticket))

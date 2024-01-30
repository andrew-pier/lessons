# Happy_Ticket

def happy_ticket(ticket):
    len_ticket = len(ticket)
    part1 = ticket[:len_ticket//2]
    part2 = ticket[len_ticket//2]
    sum1 = 0
    sum2 = 0

    for i in range(len(part1)):
        sum1 += int(part1[i])

    for i in range(len(part2)):
        sum2 += int(part2[i])
    return sum1 == sum2


ticket = input('номер билета?')
print(happy_ticket(ticket))











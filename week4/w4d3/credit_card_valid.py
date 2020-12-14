def card_validation(card_number):
    card_number = list(card_number)
    for i in range(0,len(card_number)):
        card_number[i] = int(card_number[i])

    check_digit = card_number.pop(-1)
    card_number = card_number[::-1]
    for i in range(0,len(card_number)):
        if i % 2 == 0:
            card_number[i] = card_number[i] *2
    for i in range(0,len(card_number)):
        if card_number[i] > 9:
            card_number[i] = (card_number[i] - 9)
    card_number = sum(card_number)
    card_number = card_number % 10
    return card_number == check_digit
card_validation('45567375868')
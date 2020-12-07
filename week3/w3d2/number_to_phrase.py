


ones = {
    0: '',
    1: 'one',
    2: 'two', 
    3: 'three',
    4: 'four', 
    5: 'five',
    6: 'six', 
    7: 'seven',
    8: 'eight',
    9: 'nine',
}
teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}
tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifity',
    6: 'sixty', 
    7: 'seventy',
    8: 'eighty', 
    9: 'ninty'
}

def number_phrase(number_input):
    if number_input == 0: return 'zero'
    elif number_input >= 10 and number_input <= 19:
        return teens[number_input]
    a = number_input//100
    c = number_input % 10
    b = (number_input % 100)//10
    x = ''
    y = ''   
    if b == 0 and c == 0:
        x = ones[a] + " hundred "     
    elif b != 0:        
        x = ones[a] + "hundred and " 
    if b <= 1: 
        y = ones[number_input%100]
        
    elif b > 1: 
        y = tens[b] + ones[c]
    xy = x + y 
    return xy
def main():

    while True:
        number_input = int(input('Enter your number to turn to English word: '))
        print(number_phrase(number_input))
main()
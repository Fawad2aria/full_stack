


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
def number_pharse(number_input):
    if number_input == 0: return 'zero'
    # a = number_input//100
    # d = (number_input%100)//10
    c = number_input % 10
    b = ((number_input % 100)-c) / 10
    a = ((number_input%1000)-(b*10)-c)/100

    
    
    t = ''
    h = ''
    
    if b == 0 and c == 0:
        t = ones[a] + " hundred "     
    elif b != 0:        
        t = ones[a] + "hundred and " 
    if b <= 1: 
        h = ones[number_input%100]
        # if number_input >=10 and number_input <=19:
        #     print(teens[number_input])    
    elif b > 1: 
        h = tens[b] + ones[c] 
    st = t + h 
    return st
# def num_phars(number_input):
#     # a = number_input//100
#     c = number_input % 10
#     b = (number_input % 100) / 10
#     if b < 1: 
#         j = ones[c]
#     return j
def main():

    while True:
        number_input = int(input('Enter your number to turn to English word: '))
        # c = number_input % 10
        # b = (number_input % 100) / 10 
       
        # if number_input == 0 - 9:
        print(number_pharse(number_input))
main()
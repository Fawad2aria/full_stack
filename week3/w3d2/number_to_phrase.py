ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = {10: 'ten',11: 'eleven',12: 'twelve',13: 'thirteen',14: 'fourteen',15: 'fifteen',16: 'sixteen',17: 'seventeen',18: 'eighteen',19: 'nineteen'}
tens = ['', 'ten','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def number_phrase(input_num):
    ones_degit = input_num % 10
    tens_degit = int((input_num % 100)/10)
    hundred_degit = int(input_num/100) 

    if input_num >=100:
        return ones[hundred_degit] + ' hundred ' + tens[tens_degit] + ones[ones_degit]
    elif input_num > 19:        
        return tens[tens_degit] + ones[ones_degit]
    elif input_num >= 10 and input_num <= 19:
        return teens[input_num]
    elif input_num >= 1: 
        return ones[ones_degit]
    if input_num == 0: return 'zero'
def main():
    while True:
        to_exit = input('press enter to continue or enter "done" to exit: ')
        if to_exit == "done":
            print('See you later')
            break
        input_num = int(input('Enter your number to turn to English word: '))
        print(number_phrase(input_num))
if __name__ == "__main__":
    main()  

'''
# Teacher version

ONES = dict(zip(range(10), ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))
TENS = dict(zip(range(10), ['', 'ten', 'twenty', 'thirty', 'forty', 'sixty', 'seventy', 'eighty', 'ninety']))
TEENS = dict(zip(range(10,20), ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixtenn', 'seventeen', 'eighteen', 'nineteen']))
def n2p(x):
    ones_digit = x % 10
    tens_digit = x // 10 if x < 100 else (x % 100) // 10
    hundreds_digit = x // 100

    hundreds_word = ONES.get(hundreds_digit, '')
    tens_word = TENS.get(tens_digit, '')
    ones_word = ONES[ones_digit]
    if x>100:
        return f'{hundreds_word}-hundred-{tens_word}-{ones_word}'

    elif x>19:
        return f'{tens_word}-{ones_word}'
    
    elif x>9:
        return TEENS[x]
    else:
        return ones_word
print(n2p(9))
'''
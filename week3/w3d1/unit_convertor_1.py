

'''
unit_s = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1, 
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254,
}
while True:
    greeting = input('Welcome! press "enter key" to continue or "done" to quit. ')
    if greeting == 'done':
        print('goodbye')
        break
    distance = int(input('what is the distance? '))
    unit_input = input('what are the input units? ')
    user_output = input('what are the output units? ')
    unit = unit_s[user_input]
    unit_2 = unit_s[user_output]
    total = user * unit
    total_2 = total / unit_2
    print(f'{user} {user_input} is {total_2:.4f} {user_output}')
'''
dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254
}
def dictionary(distance, unit_input, unit_output):
    unit = dict[unit_input]
    unit_2 = dict[unit_output]
     
    
    return (distance * unit) / unit_2
    

def main():
        
    while True:
        greeting = input('Welcome! press "enter key" to continue or "done" to quit. ')
        if greeting == 'done':
            print('goodbye')
            break
        distance = int(input('what is the distance? '))
        unit_input = input('what are the input units? ')
        unit_output = input('what are the output units? ')
        # print(f'{distance} {unit_input} is this output: ') 
        print((f'{distance} {unit_input} is'), dictionary(distance, unit_input, unit_output), (f'{unit_output}'))

if __name__ == "__main__":
    main()



















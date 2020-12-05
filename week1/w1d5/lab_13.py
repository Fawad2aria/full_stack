while True:
    user = input('Enter "encrypt" or "decrypt": ')
    if user == 'encrypt':
        shift = int(input('Enter your Shift number: '))
        text = input('Enter your text: ')
        encryted_text = ''
        for ch in text: 
            if ch == '':
                encryted_text += ch
            elif ch.isupper():
                encryted_text += chr((ord(ch) + shift - 65) % 26 + 65)
            else:
                encryted_text += chr((ord(ch) + shift - 97) % 26 + 97)
        print(encryted_text)
    elif user == 'decrypt':
        new_string = ''
        original = input('Enter a word: ')
        def shift(ch):
            ascii_code = ord(ch)
            new_char = ascii_code + 13
            if new_char > ord('z'):
                new_char -= 26
            new_char = chr(new_char)
            return new_char
        for ch in original:
            new_string += shift(ch)
        print(new_string)
    again = input('Do you want to play again? y/n: ')
    if again == 'y':
        user = input('Enter "encrypt" or "decrypt": ')
    elif again == 'n':
        print('goodbye')
        break 




'''
def check_palindrome(word):
    word_to_reverse = ''.join(reversed(word))
    
    return word == word_to_reverse
        
    # if word == reversed_pal:
    #     return True
    # return False
print(check_palindrome('racecar'))
'''
def check_anagram(first_word, second_word):
    # second_word = second_word.lower().replace(' ','')
    return sorted(first_word) == sorted(second_word.replace(' ','').lower())


print(check_anagram('anagram', 'Nag a Ram'))

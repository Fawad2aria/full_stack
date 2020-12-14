f = open('book123.txt')
txt = f.read()
# txt = "i went shopping yesterday and I bought one pound of apples. I also went to shopping mall to get some clotes."
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
def ari(txt):
    chars = len(txt)
    words = len(txt.split())
    sentences = len(txt.split('.'))
    ari_result = round(4.71*(chars/words)+0.5*(words/sentences)-21.43)
    if ari_result <= 14:
        return f'The ARI Book123.txt is {ari_result}\nthis cooresponds to a ' + (ari_scale[ari_result]['grade_level']) + ' level of difficulty \nthat is suitable for an average person '+ (ari_scale[ari_result]['ages'])+ ' years old.'
print(ari(txt))
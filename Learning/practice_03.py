# 03.01 Multiline string

sentence = '''
Darling,
I will be loving you
till were 70
'''    # can change ''' to """

print(sentence)

# 03.02 Slicing

data = "20231009EdSheeran"

print('year : ' + data[0:4])      # from position 0 to position 3
print('singer : ' + data[8:])     # from position 8 to the end
print('singer : ' + data[-9:])    # on the contrary

# 03.03 String methods

lyrics = 'Sing us a song, you\'r the piano man'

print(lyrics.lower())         # in lowercase
print(lyrics.upper())         # in capital
print(lyrics[0].isupper())    # position 0 is capital
print(len(lyrics))            # length of string, without backslash
print(lyrics.replace('piano man', 'pianist'))

index = lyrics.index('u')    # 1st position of u
print(index)
print(lyrics.find('u'))
print(lyrics.find('b'))      # string has no b
print(lyrics.count('u'))     # count all u in string

index = lyrics.index('u', index + 1)    # 2nd position of u
print(index)

# 03.04 String format

# use ' % '
print('I got %d problems singing' % 99)            # %d - int type
print('I %cot 99 problems singing' % 'g')          # %c - only one letter
print('I got 99 %s singing' % 'problems')          # %s - str type
print('I got %s %s singing' % (99, 'problems'))    # write in order

# use ' {} '
print('I got {} problems singing'.format(99))
print('I got {num} problems singing'.format(num = 99))
print('I got {} {} singing'.format(99, 'problems'))
print('I got {1} {0} singing'.format(99, 'problems'))    # following number in bracket

num = 99
word = 'problems'
print(f'I got {num} {word} singing')
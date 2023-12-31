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

# 03.05 Escape code

print('Not a \"Yes, sir\", not a follower')    # \" - use ', ", \
print('Not a "Yes, sir", \nnot a follower')    # \n - new line
print('Not a "Yes, sir",\r not a follower')    # \r - return cursor to initial
print('Not a "Yes, sir",\b not a follower')    # \b - remove one letter
print('Not a "Yes, sir",\t not a follower')    # \t - make long space

# 03.06 Quiz

"""
Write a program that creates a password for each website.
However, you must meet the following requirements.

1. Use SLD
2. Create as first 3 letter + length + number of e + '!'
"""

url = 'https://www.google.com'

name = url[url.index('.') + 1:]
name = name[:name.index('.')]
pw = name[:3] + str(len(name)) + str(name.count("e")) + '!'

print(f'Password of {url} is \'{pw}\'')
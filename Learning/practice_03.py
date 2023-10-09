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
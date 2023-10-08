# 01.01 Numberic data type

print(type(5))         # int type
print(type(3.14))      # float type
print(type(4 + 5j))    # complex type

# 01.02 String data type

print('Marigold')    # use ' for str type
print("Shutter")     # use " for str type
print('A'*4)         # repeat text use *int

# 01.03 Boolean data type

print(5 > 10)          # False
print(5 < 10)          # True
print(True)            # True
print(not True)        # False
print(not (5 > 10))    # True

# 01.04 Variable

print('This song is Attention by Charle Puth')
print('Charle Puth is 31')
print('Is Charlie Puth in his 30s? True')

name = 'Charle Puth'
age  = 31
generation_30s = age >= 30 and age < 40

print('This song is Attention by ' + name)    # fix string to variable
print(name + ' is ' + str(age))               # convert int type into str type
print('Is', name, 'in his 30s?', generation_30s)    # use , instead of +

# 01.05 Comment

# single line commet
'''
multy
line
comment
'''
# multy
# line
# comment

# 01.06 Quiz

"""
Use the variables to output the following statement

Variable name
 : airport

Variable value
 : 'Denver', 'Miami', 'San Jose'

Output
 : Board your flight to XXX at gate 8
"""

airport = 'Denver'
print('Board your flight to ' + airport + ' at gate 8')
airport = 'Miami'
print('Board your flight to ' + airport + ' at gate 8')
airport = 'San Jose'
print('Board your flight to ' + airport + ' at gate 8')
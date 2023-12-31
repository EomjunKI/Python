# 04.01 List

playlist = ['stay', 'bones', 'attention']
print(playlist)
print(playlist.index('bones'))    # position of bones
playlist.append('feelings')       # add 'feelings' at last
print(playlist)
playlist.insert(1, 'YOUTH')       # add 'YOUTH' at position 1
print(playlist)
print(playlist.pop())             # data at last position
print(playlist)
playlist.append('stay')
print(playlist)
print(playlist.count('stay'))     # count 'stay'

playlist.sort()                   # ascending order
print(playlist)
playlist.reverse()                # reverse order
print(playlist)
playlist.clear()                  # clear list
print(playlist)

# 04.02 Dictionary

playlist = {'A-1':'stay', 'A-2':'bones'}
print(playlist['A-1'])
print(playlist.get('A-1'))
print(playlist.get('A-3'))
print(playlist.get('A-3','avilable'))
print('A-3' in playlist)
playlist['A-3'] = 'attention'    # add key & value
print(playlist)
playlist['A-3'] = 'YOUTH'        # replace value
print(playlist)
del playlist['A-1']              # delete key & value
print(playlist)
print(playlist.keys())           # show all key
print(playlist.values())         # show all value
print(playlist.items())          # show all key & value
playlist.clear()                 # clear dictionary
print(playlist)

# 04.03 Tuple

(L_1, L_2, L_3) = ('wish', 'you', 'the best')
print(L_1, L_2, L_3)

# 04.04 set
playlist_A = ['dangerously', 'hero', 'high', 'unholy', 'stronger']
pl_1 = {'dangerouly', 'hero', 'high'}
pl_2 = set(['hero', 'stronger'])

print(pl_1 & pl_2)     # and
print(pl_1.intersection(pl_2))
print(pl_1 | pl_2)     # or
print(pl_1.union(pl_2))
print(pl_1 - pl_2)     # subtract
print(pl_1.difference(pl_2))
pl_2.add('high')       # add element
print(pl_2)
pl_1.remove('hero')    # delete element
print(pl_1)

# 04.05 Convert collection

pl_1 = tuple(pl_1)
print(pl_1, type(pl_1))
pl_1 = list(pl_1)
print(pl_1, type(pl_1))    # convert set, list, tuple

# 04.06 Quiz
"""
Write lottery program.
However, you must meet the following requirements.

1. Choose one special number from 1 to 49.
2. Choose five numbers form 1 to 49.
3. No overlap.
4. Use sample of the random module.

Output
========Winning numbers========
special : XX
numbers : [XX, XX, XX, XX, XX]
===============================
"""

from random import *
num = list(range(1,50))
win_num = sample(num, 6)
print('========Winning numbers========')
print('special : {}'.format(win_num[0]))
print('numbers : {}'.format(win_num[1:]))
print('===============================')
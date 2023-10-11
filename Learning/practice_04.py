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
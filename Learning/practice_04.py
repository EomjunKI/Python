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
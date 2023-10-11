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
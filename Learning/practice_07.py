# 07.01 STDIO

print('As', 'You', 'Are')
print('As', 'You', 'Are', sep='_')
print('As', 'You', 'Are', sep='_', end = '!')   # do not change the line
print('Chalie Puth')

import sys
print('As', 'You', 'Are', file=sys.stdout)  # Use to display outout messages
print('As', 'You', 'Are', file=sys.stderr)  # Use to display error messages

playlist = {'Symphony':'Clean Bandit', 'Love Yourself':'Justin Bieber'}
for Title, Singer in playlist.items():
    print(Title.ljust(15), Singer.rjust(15), sep=':')

for num in range(1,11):
    print('Playlist Number : ' + str(num).zfill(3))
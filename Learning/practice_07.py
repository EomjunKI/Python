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
    print('Playlist Number : ' + str(num).zfill(3)) # fill remaining space with zero

# 07.02 Output format

print('{0: >10}'.format(500))     # leave 10 space & output 500 right sorted
print('{0: >+10}'.format(-500))   # output sign & 500
print('{0:_<+10}'.format(500))    # leave 10 space & output 500 left sorted
print('{0:,}'.format(10000000))
print('{0:+,}'.format(10000000))
print('{0:^<+15,}'.format(10000000))
print('{0:f}'.format(5/3))
print('{0:.2f}'.format(5/3))
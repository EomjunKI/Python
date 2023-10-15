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

# 07.03 File IO

playlist_file = open('playlist.txt', 'w',)  # file to write
print('Symphony : Clean Bandit', file=playlist_file)    # automatic line change
print('Love Yourself : Justin Bieber', file=playlist_file)
playlist_file.close()

playlist_file = open('playlist.txt', 'a',)  # file to write continually
playlist_file.write('Photograph : Ed Sheeran\n')    # not automatic line change
playlist_file.write('Demons : Imagine Dragons')
playlist_file.close()

playlist_file = open('playlist.txt', 'r')   # file to read
print(playlist_file.read()) # read all
playlist_file.close()

playlist_file = open('playlist.txt', 'r')
print(playlist_file.readline()) # read single line, Move cursor to next
print(playlist_file.readline())
print(playlist_file.readline(), end='')
print(playlist_file.readline())
playlist_file.close()

playlist_file = open('playlist.txt', 'r')
while True:
    line = playlist_file.read()
    if not line:
        break
    print(line)
playlist_file.close()

playlist_file = open('playlist.txt', 'r')
lines = playlist_file.read()
for line in lines:
    print(line, end='')
playlist_file.close()
# 06.01 Function

def add_playlist():    # define new funtion
    print('Add a new song.')

add_playlist()

# 06.02 Input & Return

def num_song(num, num_new):
    print('Number of song in playlist : {}'.format(num + num_new))
    return num + num_new

num = 30    # number of song in playlist already
num = num_song(num, 20)
print(num)

# 06.03 Default value

def profile(song, singer):
    print('Title : {}\t Singer : {}'.format(song, singer))

profile('That\'s Hilarious', 'Charlie Puth')
profile('Dangerously', 'Charlie Puth')

def profile1(song, singer='Charlie Puth'):    # use repeated inputs
    print('Title : {}\t Singer : {}'.format(song, singer))

profile1('That\'s Hilarious')
profile1('Dangerously')
profile1('Goodbyes', 'Post Malane')

# 06.04 Keyword

profile(singer = 'Post Malane', song = 'Goodbyes')

# 06.05 Variable factor

def profile_2(singer, *song):
    print('singer : {}\t'.format(singer),end=' ')
    for songs in song:
        print(songs, end=' ')
    print()

profile_2('Charlie Puth', 'That\'s Hilarious', 'Dangerously')
profile_2('Post Malane', 'Goodbyes')

# 06.06 Local & Global variables

num_song = 10

def add_song(new):
    num_song = 30    # use only in function
    num_song = num_song + new
    print('Number of songs in playlist : {}'.format(num_song))

print('Number of songs in playlist : {}'.format(num_song))
add_song(4)
print('Number of songs in playlist : {}'.format(num_song))

def add_song(new):
    global num_song    # use global variable
    num_song = num_song + new
    print('Number of songs in playlist : {}'.format(num_song))

print('Number of songs in playlist : {}'.format(num_song))
add_song(4)
print('Number of songs in playlist : {}'.format(num_song))

def add_song_return(num_song, new):    # global variable as input
    num_song = num_song + new
    print('Number of songs in playlist : {}'.format(num_song))
    return num_song

print('Number of songs in playlist : {}'.format(num_song))
num_song = add_song_return(num_song, 4)
print('Number of songs in playlist : {}'.format(num_song))
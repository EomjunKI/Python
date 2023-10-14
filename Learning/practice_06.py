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
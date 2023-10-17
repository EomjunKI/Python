# 09.01 Exception

try:
    playlist = ['dangerously', 'hero', 'high']
    num = 4
    print(playlist[num-1])  # line that error occurred
except IndexError:
    print(f'There\'s no position {num-1}')  # Output when error occurs

# 09.02 Raise

try:
    num_list = [0, 1, 2]
    num = 4
    if num > 3:
        raise ValueError
except ValueError:
    print('over 3') 

# 09.03 User-defined exceptions

class DefinedError(Exception):  # inherit exception
    pass

try:
    num = 6
    if num > 3 :
        raise DefinedError
    print(f'{num}')
except DefinedError:
    print('DefinedError')
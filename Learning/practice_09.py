# 09.01 Exception

try:
    playlist = ['dangerously', 'hero', 'high']
    num = 4
    print(playlist[num-1])  # line that error occurred
except IndexError:
    print(f'There\'s no position {num-1}')  # Output when error occurs
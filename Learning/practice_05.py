# 05.01 If

weather = 'snowy'
if weather == 'rainy' or weather == 'snowy':
    print('Bring umbrella')
elif weather == 'sunny':
    print('Put on sunscreen')
else :
    print('Just go outside')

temp = 27
if temp >= 30:
    print('Hot')
elif temp >= 20 & temp <30:
    print('Warm')
elif temp >= 10 & temp <20:
    print('Cool')
else : 
    print('Cold')

# 05.02 For

playlist = ["STAY", "Flowers", "Attention"]
for song in playlist:
    print("song : {}".format(song))

for playlist_num in range(5): # until 5th
    print("number of playlist : {}".format(playlist_num))
for playlist_num in range(1,5): # 1 or more and less than 4
    print("number of playlist : {}".format(playlist_num))

# 05.03 Whlie

num = 0
result = 0
while num < 10:
    print(num, result)
    num += 1
    result += num
print(result)

# 05.04 Continue & Break

exception = [3, 5]
end_sequence = [7]
for num in range(10):
    if num in exception:
        continue    # pass
    elif num in end_sequence:
        break       # stop
    print(num)

# 05.05 Single line for loop

playlist = ["STAY", "Flowers", "Attention"]
playlist_len = [len(i) for i in playlist]
print(playlist_len)

# 05.06 Quiz

"""
You are Uber driver.
Write a program that to find the number of passengers on board.
However, you must meet the following requirements.

1. Total number of passengers is 50
2. Time required for each passenger is random between 5 and 50 min
3. Match time required between 5 and 15 min

Output sample
[O] 1st passenger (Time required : 7 min)
[ ] 2nd passenger (Time required : 32 min)
[O] 3rd passenger (Time required : 8 min)
 ...
[ ] 50th passenger (Time required : 20 min)

number of passengers on board : XX
"""

from random import *

count = 0

for num in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        if num%10 == 1 and num != 11:
            print('[O] {}st passenger (Time required : {})'.format(num, time))
            count += 1
        elif num%10 == 2 and num != 12:
            print('[O] {}nd passenger (Time required : {})'.format(num, time))
            count += 1
        elif num%10 == 3 and num != 13:
            print('[O] {}rd passenger (Time required : {})'.format(num, time))
            count += 1
        else :
            print('[O] {}th passenger (Time required : {})'.format(num, time))
            count += 1
    else:
        if num%10 == 1 and num != 11:
            print('[ ] {}st passenger (Time required : {})'.format(num, time))
        elif num%10 == 2 and num != 12:
            print('[ ] {}nd passenger (Time required : {})'.format(num, time))
        elif num%10 == 3 and num != 13:
            print('[ ] {}rd passenger (Time required : {})'.format(num, time))
        else :
            print('[ ] {}th passenger (Time required : {})'.format(num, time))
            
print('number of passengers on board : {}'.format(count))
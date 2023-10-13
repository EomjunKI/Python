# 05.01 if

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

# 05.02 for

playlist = ["STAY", "Flowers", "Attention"]
for song in playlist:
    print("song : {}".format(song))

for playlist_num in range(5): # until 5th
    print("number of playlist : {}".format(playlist_num))
for playlist_num in range(1,5): # 1 or more and less than 4
    print("number of playlist : {}".format(playlist_num))

# 05.03 whlie

num = 0
result = 0
while num < 10:
    print(num, result)
    num += 1
    result += num
print(result)
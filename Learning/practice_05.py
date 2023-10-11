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
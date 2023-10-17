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

# 09.04 Finally

try:
    num = 8
    if num > 4:
        raise
except RuntimeError:
    print('RuntimeError')
finally:    # certainly output
    print('program end')

# 09.05 Quiz

'''
Write a program that automated ordering system for waiting.
However, you must meet the following requirements.

1. All customers can order up to 10 chicken in total.
'''

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print(f'Remaining Chicken : {chicken:<2}')
        order = int(input('How many would you like to order?'))
        if order > chicken:
            print('lack of ingredients')
        elif order <= 0:
            raise ValueError
        else:
            print(f'[Waiting : {waiting:<2}]') 
            print(f'Your order for {order:<2} chickens has been completed')
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
        
    except ValueError:
        print('Enter an incorrect value')

    except SoldOutError:
        print('ingredients are exhausted.')
        break
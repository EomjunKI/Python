# 02.01 Operator

# arithmetic operator
a = 5
b = 2

print(a + b)     # additon
print(a - b)     # subtraction
print(a * b)     # multiplication
print(a / b)     # division
print(a ** b)    # exponentiation
print(a % b)     # remainder
print(a // b)    # quotient

# comparison operator
print(10 > 3)     # over / under
print(3 >= 10)    # more than / less than
print(3 == 3)     # equal
print(3 != 3)     # not equal

# 02.02 Mathematical expression
num = 14
print(num)
num += 2    # same as 'num = num + 2'
print(num)
num *= 2    # same as 'num = num * 2'
print(num)
num /= 2    # same as 'num = num / 2'
print(num)
num -= 2    # same as 'num = num - 2'
print(num)
num %= 2    # same as 'num = num % 2'
print(num)

# 02.03 Mathematical functions

# builtin function
print(abs(-5))
print(pow(3, 2))    # pow(base,power)
print(max(5, 2))
print(min(5, 2))
print(round(3.14))
print(round(3.8))

# module function
from math import *
print(floor(3.14))    # round down
print(ceil(3.14))     # round up
print(sqrt(16))

# 02.04 Random function

from random import *

print(random())    # 0.0 <= float type value < 1.0
print(randrange(1, 10))    # 1 <= int type value < 10
print(randint(1, 10))    # 1 <= int type value <= 10

# 02.05 Quiz

"""
You go to the theater once a month.
Write a program that determines the day to go to the theater.
However, you must meet the following requirements.

1. Have to choose randomly.
2. Decide between 5th and 28th
"""
from random import *

date = randint(5, 28)
print('The day to go to the theater every month is the '+ str(date) +'th.')
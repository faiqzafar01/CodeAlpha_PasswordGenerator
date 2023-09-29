import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
number = '0123456789'

alpha_numb = lower + upper + number

length = 8
password = ""
for i  in range(10):
    password = "".join(random.sample(alpha_numb, length))
    print("Your AlphaNumeric Password is : ", password)
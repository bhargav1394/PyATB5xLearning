import math

def give_me_power(num):
    return math.pow(num,2)
op = give_me_power(10)
print(op)

op2 = lambda : math.pow(int(input("Enter Value")), 2)
print(op2())
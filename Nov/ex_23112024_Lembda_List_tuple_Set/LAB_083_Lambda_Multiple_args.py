#**Lambda | lambda arguments: expression**
#- A lambda is an anonymous function that returns some form of data.

def num(a,b):
    return a * b

demo = num(10, 20)
print(demo)
a_l = lambda a,b : a*b
print(a_l(5,5))

def sum_three(a,b,c):
    return a +b+c
demo = sum_three(10, 20, 40)
print(demo)
a_l = lambda a,b,c : a+b+c
print(a_l(5,5,5))
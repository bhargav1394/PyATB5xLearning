#Write a program that prints numbers from 1 to 100. However, for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz." ( for, if)

for i in range(1,101):
    if i % 3 == 0:
        if i % 5 ==0:
            print("FizzBuzz",i)
            continue
        print("Fizz",i)
    elif i % 5 == 0:
        print("Buzz",i)
    else:
        print(i)
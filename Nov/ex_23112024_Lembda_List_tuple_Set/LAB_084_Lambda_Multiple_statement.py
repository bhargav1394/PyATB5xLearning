# Write a program even and odd

def even_odd(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

even_odd(5)
check_even_odd = lambda num: "Even Number" if num % 2 == 0 else "Odd Number"
print(check_even_odd(5))
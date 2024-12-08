# Crete program to sum of three number from the user input

def sum_number(a=100,b=200,c=300):
    return a + b + c
sum = sum_number()
print(sum)
a = int(input("Enter first number\n"))
b = int(input("Enter Second Number\n"))
c = int(input("Enter third Number\n"))

sum = sum_number(a,b,c)
print("Sum of Three Numbers",sum)


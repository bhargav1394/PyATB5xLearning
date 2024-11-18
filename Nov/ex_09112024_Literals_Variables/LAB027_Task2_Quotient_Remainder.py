#Take two number and find the Quotient and Remainder

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

Quotient = a // b
Remainder = a % b
print(f"Quotient of {a} and {b} is ", Quotient)
print(f"Remainder of {a} and {b} is  ", int(Remainder))

# We are using divmod function for the same
print(divmod(a,b))

"""
Output
Enter value of a: 15
Enter value of b: 2
Quotient of 15 and 2 is  7
Remainder of 15 and 2 is   1
(7, 1)
"""
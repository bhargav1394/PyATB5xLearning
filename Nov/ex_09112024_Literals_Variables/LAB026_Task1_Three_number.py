"""
Task
Take a 3 input from the user
perform sum,sub,mul and div
"""
a = int(input("Enter Value of First Number 1 :"))
b = int(input("Enter Value of Second Number 2 :"))
c = int(input("Enter Value of Third Number 3 :"))

sum = a + b + c
sub = a - b - c
mul = a * b * c
div = a / b

print("Addition Of three Value: ", sum)
print("Subtraction Of three Value: ", sub)
print("Multiplication Of three Value: ", mul)
print("Division Of three Value: ", div)

"""
Output

Enter Value of First Number 1 :15
Enter Value of Second Number 2 :5
Enter Value of Third Number 3 :3
Addition Of three Value:  23
Subtraction Of three Value:  7
Multiplication Of three Value:  225
Division Of three Value:  3.0
"""
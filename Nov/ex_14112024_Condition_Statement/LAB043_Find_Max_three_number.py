#Write code Max number

a = float(input("Enter Value num1\n"))
b = float(input("Enter Value num2\n"))
c = float(input("Enter Value num3\n"))


if a >= b and a >= c:
    print("Max is a")
elif b >= c and b>= a:
    print ("Max is b")
else:
    print("Max is c")

#Edge cases
# if both are same print any one number
# input in string -> ABC
# -ve value -> -1
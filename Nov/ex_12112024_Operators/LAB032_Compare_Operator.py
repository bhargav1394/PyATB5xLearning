# Compression operator
# == Equal to
# < Less than
# > Greater than
# <= Less than equal to
# >= Greater than equal to
# ! Not Equal to

a = float(input("Enter First Number"))
b = float(input("Enter Second Number"))

if a <= b:
    print("First number is less than")
else:
    print("First number is Greater than")

"""output
Enter First Number20
Enter Second Number15
First number is Greater than

Enter First Number15
Enter Second Number20
First number is less than
"""
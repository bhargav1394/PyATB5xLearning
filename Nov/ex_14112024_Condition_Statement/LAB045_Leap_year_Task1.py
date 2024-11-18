#Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.

year = int(input("Enter Year:\n"))
leap_check = year % 4
if leap_check == 0:
    if year % 100 == 0:
        if year % 400 != 0:
            print("It is not a Leap Year")
        else:
            print("It is Leap Year")
    else:
        print("It is Leap Year")
else:
    print("Not Leap Year")
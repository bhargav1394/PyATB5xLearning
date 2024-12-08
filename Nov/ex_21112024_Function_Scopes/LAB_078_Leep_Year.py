# Checking for a Leap Year , 2024 → Yes
#
# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.


# The year is multiple of 400.
# The year is a multiple of 4 and not a multiple of 100.

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
        return True
    else:
        print("Not Leap year")
        return False
year = int(input("Enter Year"))
check_leap_year(year)
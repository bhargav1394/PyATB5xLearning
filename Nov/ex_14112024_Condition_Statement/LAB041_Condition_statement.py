#Write a program to take a user age and let him know if he can go the club.  21

#Logic sliding formula
#Step 1
#User input => data type int
# output => output should in string

#Step2 Rough logic
# if the age > 21 then print the can go to the club
# if the age < 21 then print you cant go to the club

#Step3 Write logic
age = int(input("Enter your age:\n"))
if (age >= 21):
    print("You can go to the club enjoy!")
else:
    print("you can't go to the club sorry")

#Steps4 Check fot the edge cases
# We should consider edge cases such as
# Negative arguments or extremely high value -> Program will break
# Non-numeric input -ABC
# Age which is valid

#Step 5 optimize the code
#Handel the all edge scenarios

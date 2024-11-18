# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#nput- score - 89
#output- B
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

result = int(input("Enter Your Score\n"))
if 90 <= result and result <= 100 :
    print("Grade A")
elif 80 <= result and result <= 89 :
    print("Grade B")
elif 70 <= result and result <= 79:
    print("Grade C")
elif 60 <= result and result <= 69:
    print("Grade D")
elif 100 <= result:
    print("You are the superman you can pass any exam")
else:
    print("Grade F")


#Edge cases
# if both are same print any one number
# input in string -> ABC
# -ve value -> -1
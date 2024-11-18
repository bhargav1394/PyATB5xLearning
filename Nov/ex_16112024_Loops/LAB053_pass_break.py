#Pass is a placeholder statement that does nothing
# It's used when a statement is syntactically required but no action is needed
for i in range(0,10,1):
    if  i == 6 or i == 5:
        print(i)
    else:
        pass

#Continue statement continue statements skips the current iteration of a loop and move to the next iteration
for i in range(0,10,5):
    if  i == 6 or i == 5:
        print(i)
    else:
        continue

#Execution like
# i | condition | O/P
# 0 | 0 == 5 => False | O/P -> Nothing will be printed
# 1 | 1 == 5 => False | O/P -> Nothing will be printed
# 2 | 2 == 5 => False | O/P -> Nothing will be printed
# 3 | 3 == 5 => False | O/P -> Nothing will be printed
# 4 | 4 == 5 => False | O/P -> Nothing will be printed
# 5 | 5 == 5 => True | O/P -> 5
# 6 | 6 == 5 => True | O/P -> 6
# 9 | 9 == 5 => False | O/P -> Nothing will be printed



for i in range(0,10):
    if  i == 5:
        print("Five")
    else:
        print(i)

#Execution like
# i | condition | O/P
# 0 | 0 == 5 => False | O/P -> 0
# 1 | 1 == 5 => False | O/P -> 1
# 2 | 2 == 5 => False | O/P -> 2
# 3 | 3 == 5 => False | O/P -> 3
# 4 | 4 == 5 => False | O/P -> 4
# 5 | 5 == 5 => True | O/P -> Five
# 9 | 9 == 5 => False | O/P -> 9
# 10 | 10 == 5 => False | For loop finished - O/P = Exit

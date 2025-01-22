# Write a program to remove Duplicate values form the list with help of set

a = [1,1,3,5,6,4,1,2,3,5,4,3]

unique_value= set()

for value in a:
    if value == unique_value:
        pass
    else:
        #b = value
        unique_value.add(value)

print(unique_value)



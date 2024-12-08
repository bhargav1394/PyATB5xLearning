## **Advance Data Structures **
### List
#- Collection of Items.
#- Duplicate are allowed.
#- Multiple different data types are allowed.
#- Stored with the Index - 0 to len-1
#-  List is Mutable in nature
#    - `my_list[1] = "Amit"print(my_list)`
#Syntax  - []
# grocery List -  butter, bread, banana, paneer.
# 10th marks - 90,91,92, 78, 56

# List - Collection  of items
# grocery List -  butter, bread, banana, paneer.
# 10th marks - 90,91,92, 78, 56

my_list = [1, 2, 3]  # Same type of data (int)
my_list2 = [1, True, "Rathod", 12.34]

print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[4]) # list index out of range


my_list[0] = "Bhargav"
my_list[1] = "Rathod"
my_list[2] = "Hirabhai"
print(my_list)

print(" -- ")

for item in my_list2:
    print(item)

print(" --- ")

for i in range(1, 5): # range( start, stop-1)
    print(i ,end=" ")

# range(1,5) -> returns List [1,2,3,4]

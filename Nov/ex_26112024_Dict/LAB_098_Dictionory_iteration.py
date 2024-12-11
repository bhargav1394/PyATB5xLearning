### Dict
#- `Accessing Values: **my_dict[key]**`
#- `Adding/Updating a Key-Value Pair: **my_dict[key] = value **`

# change the dictionary
my_dict = {"Name": "Bhargav", "Age":"30","Role": "QA", "experience": 6}

print(my_dict)
print(my_dict["Name"],my_dict["Age"],my_dict["Role"], my_dict["experience"])

my_dict["Role"] = "Wifi QA" #Modify the Dictionary
print(my_dict)

del my_dict["experience"] #Delete the dictionary key
print(my_dict)

for key,value in my_dict.items():
    print(key,"->",value)


print("Name" in my_dict)
print("experience" in my_dict)
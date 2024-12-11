### Dict from two lists

keys = ["Name","Role","experience"]
values=["Bhargav","QA",6]

com_dic = dict(zip(keys,values))

print (com_dic)
#merge Two Dictionaries

dict1 = {"a":1,"b":2}
dict2 = {"c":3, "d":4}

merged_dict = dict1 | dict2
merged_dict1 = dict2 | dict1


print(merged_dict)
print(merged_dict1)
print(merged_dict.get("a"))
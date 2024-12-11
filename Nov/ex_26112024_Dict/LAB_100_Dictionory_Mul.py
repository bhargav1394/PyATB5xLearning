### Dict
#- `Accessing Values: **my_dict[key]**`
#- `Adding/Updating a Key-Value Pair: **my_dict[key] = value **`

# change the dictionary
com_qa = {"Name": "Bhargav" , "Age":"30","Role": "WiFi QA", "experience": 6}

#print(com_qa["Name"])

#Dictionary in Dictionary with multiple list

comp1 = {"Ahmedabad_office": {"Name":"Bhargav", "age": 30, "Role": "QA"}, "Pune_office":{"Name":"Vikas", "age": 32, "Role": "WifiQA"}}
comp2 = {"Ahmedabad_office": {"Name":"Manthan", "age": 26, "Role": "Developer"}, "Pune_office":{"Name":"Ravi", "age": 30, "Role": "Senior Engineer"}}

company_list = [comp1,comp2]

print(comp1["Ahmedabad_office"])
print(company_list)
print(company_list[1]["Pune_office"]["Name"])
print(company_list[1])

#alternet way
print(comp2["Ahmedabad_office"]["Role"])
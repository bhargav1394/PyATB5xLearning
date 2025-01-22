#Remove the Duplicate values from the dictonary

dict1 = {"a":4,"b":2, "c":5, "d":3, "e":4}

unique_value = set()
result = {}

for key, value in dict1.items():
    if value not in unique_value:
        result[key] =value
        unique_value.add(value)

print(result)
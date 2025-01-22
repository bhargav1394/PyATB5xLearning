#Function that return the maximum vlaue from a dictionary

dict1 = {"a":4,"b":2, "c":5, "d":3, "e":4}

def max_value(dict):
    return max(dict.values())

def min_value(dict):
    return min(dict.values())

print(max_value(dict1))
print(min_value(dict1))
#Frequency of characters in a string
# Write a program to count the frequency of each charcter in a given string.
#ans {a:2}
#string = "automation"
string1 = input("Enter the input e.g automation")

char_count = {}

#Logic Building
#I/P -> String
#O/P -> dict

for char in string1:
    char_count[char] = char_count.get(char,0) + 1
print(char_count)

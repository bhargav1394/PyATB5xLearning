# Find the vowel from the userinput
input_a = input("Enter the word")
vowels = "aeiou"
vowels_count = 0
consonant_count = 0
result =dict()
unique_value= set()
for char in input_a:
    if char in vowels:
        result[char]= 1
        print(result)
        vowels_count += 1
    else:
        consonant_count += 1
        unique_value.add(consonant_count)



print(vowels_count)
print(unique_value)



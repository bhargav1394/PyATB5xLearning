# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

Side_1 = int(input("Enter side one"))
Side_2 = int(input("Enter side second"))
Side_3 = int(input("Enter side third"))

a = "equilateral"
b = "isosceles"
c =  "scalene"
if Side_1 == Side_2 and Side_1 == Side_3:
    print(f"Triangle is {a} because all sides are equal")
elif Side_1 == Side_2 or Side_1 == Side_3 or Side_2 == Side_3:
    print(f"Triangle is {b} because of two sides are same")
else:
    print(f"No sides are equal That's why it is {c}")

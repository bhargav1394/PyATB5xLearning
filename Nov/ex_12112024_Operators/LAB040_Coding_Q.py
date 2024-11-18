#Program to calculate the area of the circle given its radius using the formula
# '' area = pi * r^2 (Take a pi value is 3.14
#Logic building
# Step 1
# Figure out the input and output
#Input is r -> Data type -> Float
# pi value -> 3.14
# power of Input of radius -> pow or **
# output -> float area , print area
#--------------------------------------------------
#Step2
# Rough logic => area = 3.13 * r**2(pow(r,2)
#--------------------------------------------------
#Step3
#Actuall write code
radius = float(input("Enter Radius of the circle\n"))
print(radius)
#area = 3.14 * (radius**2)

area = 3.140156487 * (pow(radius,2))
print("Area of the circle is", area)

print("Using formating using 'f'")
print(f"Area of the circle is Area= {area:.2f}")


#Ternary Operator
print(3.14 * pow(float(input("Enter radius value")),2))
"""
Output
Enter Radius of the circle
10
10.0
Area of the circle is 314.0156487
Using formating using 'f'
Area of the circle is Area= 314.02

"""

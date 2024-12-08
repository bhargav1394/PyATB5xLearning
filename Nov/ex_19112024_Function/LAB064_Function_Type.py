# **User Defined**
#
# 1. `The can't return -> non return`
# 2. They can return something
# 3. They have parameters
# 4. Argument + return Type


# 1. `The can't return -> non return`
#No Return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello")
greet()

# 2. # No Return Type and with Argument/ Param
def  greet_with_Name(name):
    print("Hello,", name)
greet_with_Name("Bhargav")

# 3. No Return Type and with Default Argument ( # positional argument)

def say_hello_default_arg(name="Rathod"):
    print("Hello",name.upper())
say_hello_default_arg("Bhargav")
say_hello_default_arg()

def mul_args(name1="Bhargav",name2="Rathod"):
    print("Multiple Args", name1, name2)

mul_args()
mul_args("Hello")
mul_args("Demo","Hello")
mul_args(name2="only_oneArgs")

# 4. Argument + return Type

def sum_of_two_number_with_default(num1=100, num2=200):
    return num1 + num2

result = sum_of_two_number_with_default()
print(result)
result = sum_of_two_number_with_default(68,78)
print(result)
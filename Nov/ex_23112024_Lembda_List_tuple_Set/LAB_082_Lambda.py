#**Lambda | lambda arguments: expression**
#- A lambda is an anonymous function that returns some form of data.
#Syntax: The syntax to create a lambda function is **lambda arguments: expression**.
# The lambda keyword is used to define the anonymous function,
# followed by a list of arguments, a colon, and an expression.

#**Arguments**: Like a **normal function**, a lambda function can accept any number of arguments
# but must have only one expression. The arguments are specified before the colon.

#**Expression**: The expression is executed and the **result is returned**
# when the lambda function is called. This expression is written after the colon.
#If you have Multiple statements - Lambda is not recommended.



def lembda_demo(num):
    return num ** 3

a = lembda_demo(2)
print(a)

a_l = lambda num: num ** 3
print(a_l(5))
#Outer functions - vars can be used by the inner functions.


def outer_function():
    var1 = 10 # Local Variable
    def inner_function():
        print(var1)
        var2 = 20
        print(var2)
    def inner_function2():
        print(var1)
        var2 =30
        print(var2)
    inner_function()
    inner_function2()
outer_function()

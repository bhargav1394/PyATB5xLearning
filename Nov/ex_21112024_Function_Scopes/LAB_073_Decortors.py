#**Understanding Decorators in Python**

#- You can add a Annotation to the functions(to perform the extra task)
#- e.g -> before running the function I want to do something ( decorators)

#Decorators in Python are a powerful and flexible tool that allows you to modify the behavior
#of functions or methods without changing their actual code.
#They are essentially functions that take another function as an argument and extend or alter its behavior.
#Pre and post report we can use the decorator

def add_security(func):

    def wrapper():
        print("If you Driver you should were helmet, Bring the All documents")
        func()
        print("If you done your driving then you can leve it all document safe place")
    return wrapper()

@add_security
def drive_car():
    print("Driving the car")

@add_security
def driving_scooty():
    print("Normal Driving")

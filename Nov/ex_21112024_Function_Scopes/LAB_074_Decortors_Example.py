#Pre and post report we can use the decorator

def add_before_ui_after_ui(func):

    def wrapper():
        print("Before Running UI ")
        print("Starting browser")
        func()
        print("Ending the testing")
        print("Quit the Browser")
    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print("I am testing the UI of this webpage")

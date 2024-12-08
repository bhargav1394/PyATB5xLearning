import time

def time_decor(fun):

    def wrapper():
        start_time = time.time()
        print(f"{start_time:.2f}")
        fun()
        end_time = time.time()
        print(f"{end_time:.2f}")
        Total_time = end_time - start_time
        print(f"Total time take this function: {Total_time:.2f} ")
    return wrapper()

def print_deco(func):
    def wrapper():
        print("starting Logs")
        func()
        print("Ending Logs")
    return wrapper()

@print_deco
@time_decor
def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)

@time_decor
def test_ui_2():
    print("Add a function, time taken by this function 2 ")
    time.sleep(5)
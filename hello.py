
def decorator(func):
    def wrapper():
        print("hey")
        func()
        print("out")
    return wrapper


@decorator
def greet():
    print("hello, ")

greet()
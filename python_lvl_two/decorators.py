# Decorators can be thought of as functions which modify the
# functionality of another function

def hello(name="jose"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")
    def greet():
        return "THIS STRING IS INSIDE GREET()"
    def welcome():
        return "THIS STRING IS INSIDE WELCOME()"

    if name == "jose":
        return greet
    else:
        return welcome


# x = hello()
# print(x())


def hi():
    return "HI JOSE!"

def other(func):
    print("HELLO!")
    print(func)
    print(func())

# other(hi)

# Decorator function

def new_decorator(func):
    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")

# print("Before:")
# func_needs_decorator()
# print("After:")
# func_needs_decorator = new_decorator(func_needs_decorator) == @new_decorator
func_needs_decorator()

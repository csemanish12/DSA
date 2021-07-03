# Decorators are very powerful and useful tool in Python since it
# allows programmers to modify the behavior of function or class.
# Decorators allow us to wrap another function in order to extend the
# behavior of the wrapped function, without permanently modifying it

# functions are first-class objects. This means that functions can be passed
# around and used as arguments, just like any other
# object (string, int, float, list, and so on).

# simple decorators
import functools


def my_decorator(func):
    def wrapper():
        print("something is happening before the function")
        func()
        print("something is happening after the function")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


# *args and **kwargs in the inner wrapper function. Then it will accept an arbitrary number
# of positional and keyword arguments
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def greet(msg):
    print(msg)


# say_whee = my_decorator(say_whee) this is same as using decorator
say_whee()
greet("hello world")


# Returning Values from Decorated functions
@do_twice
def return_greeting(name):
    print("creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("adam")
print(hi_adam)


# here , the decorator ate the return value from the function.
# Because the do_twice_wrapper() doesn’t explicitly return a value,
# the call return_greeting("Adam") ended up returning None.
# to fix this, we need to make sure the wrapper function returns the return
# value of the decorated function

def do_twice_fixed(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@do_twice_fixed
def return_greeting_v2(name):
    print("creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting_v2("adam")
print(hi_adam)

# who are you, really?
# function.__name__ and help(function) gives you name and documentation of function
print('get name of function:', return_greeting_v2.__name__)
print('docs of function:', help(return_greeting_v2))


# the name and docs are of functino wrapper instead of actual function
# to fix this, decorators should use @functools.wraps decorator, which will
# preserve information about the original function.

def do_twice_updated(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@do_twice_updated
def return_greeting_v3(name):
    print("creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting_v3("adam")
print(hi_adam)
print('get name of function:', return_greeting_v3.__name__)
print('docs of function:', help(return_greeting_v3))


# now its fixed

# Decorators with Arguments
def repeat(number):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_function(*args, **kwargs):
            for _ in range(number):
                value = func(*args, **kwargs)
            return value

        return wrapper_function

    return decorator_repeat


@repeat(number=4)
def greet(name):
    print(f"Hello {name}")


greet("adam")

"""Write a Python program to detect the number of local variables declared in a function."""

def count_local_vars(func):
    return func.__code__.co_nlocals
def my_function():
    x = 1
    y = 6
    i = 15
    return x + y + i
print(count_local_vars(my_function))

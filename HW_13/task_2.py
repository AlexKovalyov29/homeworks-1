"""Write a Python program to access a function inside a function (Tips: use function, which returns another function)"""

def outer_function(x):
    def inner_function(y):
        return x * y
    return inner_function
result = outer_function(15)
print(result(5))

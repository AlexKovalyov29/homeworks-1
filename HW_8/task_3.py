""" simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
(to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as
the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.
For example:
the call make_operation('+', 7, 7, 2) should return 16
the call make_operation('-', 5, 5, -10, -20) should return 30
the call make_operation('*', 7, 6) should return 42  """

def make_operation_sum (x,y):
    return x+y+x
print(make_operation_sum(7,2))

def make_operation_subtraction (x,y,s):
    return x-x-y-s
print(make_operation_subtraction(5,-10,-20))

def make_operation_multiplication (x,y):
    return x*y
print(make_operation_multiplication(7,6))
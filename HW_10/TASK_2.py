"""Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block which raises an exception
if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero)."""

def twonumbers():
    try:
        a = float(input("Your a: "))
        b = float(int(input("Your b:")))
        return (a**2)/b
    except ValueError:
        print("error, it`s not a number ")
    except ZeroDivisionError:
        print("error, you can`t divide by zero")
answer = twonumbers()
if answer is not None:
    print(f"Results = {answer}")
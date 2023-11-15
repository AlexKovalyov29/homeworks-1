"""Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?"""


def oops():
    raise IndexError("oops, IndexError")
try:
    oops()
except IndexError as i:
    print(f"Error detected: {i}")


def oops():
    raise KeyError("oops, KeyError")
try:
    oops()
except IndexError as i:
    print(f"Error detected: {i}")
except KeyError as i:
    print(f"Error detected: {i}")


import random

def generate_random_strings(input_string, num_strings):
    for _ in range(num_strings):
        random_string = ''.join(random.sample(input_string, len(input_string)))
        print(random_string)

input_string = "Hello"
generate_random_strings(input_string, 5)





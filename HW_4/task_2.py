# С номерами телефонов
#my_input = input("Your phone number")
#print("Number",my_input)
#if my_input.startswith('a:'):
#    print("ok")

my_input = ''
number_is_valid = False
while not number_is_valid:
    my_input = input("Your number phone started : ")
    print("Your number:",my_input)
    if not my_input.startswith('0'):
        print('Wrong number')
    elif len(my_input) != 10:
        print("wrong number len")
    else:
        number_is_valid = True
        print("number is true")



# задать количество чисел не получаеться

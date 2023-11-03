"""                                 Task 2
                        Doggy age
Create a class Dog with class attribute 'age_factor' equals to 7.
Make __init__() which takes values for a dog’s age. Then create a method `human_age`
which returns the dog’s age in human equivalent."""

class Dog:
    def __init__(self,name,age):   #human_age
        self.name = name
        self.age = age
#        self.human_age =
    def talk (self):
        print(f'My dog {self.name} age is {self.age}, but if a dog were a human his age would be {self.age *7 } ')
my_dog = Dog('Sharik', 3,)
print(my_dog.talk())

# как и в первом задании, не знаю почему высвечивает None в консоли
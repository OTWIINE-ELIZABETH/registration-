class Dog:

    def __init__(self, name, breed, age):
    
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("Woof!")

    def fetch(self):
        print("Fetching!")

    def __str__(self):
        print( f"{self.name} is a {self.breed} who is {self.age} years old.")
    
dina = Dog("dina", "breed", 1)

dina.__str__()



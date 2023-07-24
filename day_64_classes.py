# declare a class
class Animals:
    # the class attributes
    species = None
    name = None
    continent = None
    sound = None

    # initialise the class. this is like a constructor
    def __init__(self, species, name, continent, sound):
        self.name = name
        self.species = species
        self.continent = continent
        self.sound = sound

    # create a class function. an animal with a name will talk
    def talk(self):
        print(f"""{self.name} says {self.sound}""")


# make a cat from the class animals
cat = Animals("cat", "jon", "asia", "meow")
print(cat.name)
# use the cat with the class function talk()
cat.talk()

# make a Zebra
zebra = Animals("zebra", "strippy", "africa", "bleet")
# make the zebra talk
zebra.talk()


# extend a class.
# extend the animal class with a bird class
class Bird(Animals):
    movement = None

    def __init__(self, movement, species, name, continent, sound):
        super().__init__(species, name, continent, sound)
        self.movement = movement

    def fly(self):
        print(f"""{self.name} moves by {self.movement} """)


polly = Bird("flying", "avian", "polly", "earth", "tweet")
polly.talk()
polly.fly()


class animal:
    species = None
    name = None
    sound = None
    color = None

    def __init__(self, name, species, sound, color):
        self.name = name
        self.species = species
        self.sound = sound
        self.color = color

    def talk(self):
        print(f"{self.name} is a {self.color} {self.species} and says {self.sound}")


class bird(animal):

    def __init__(self, color):
        self.name = "Bird"
        self.species = "Avian"
        self.sound = "Tweet"
        self.color = color


cow = animal("Ermintrude", "Bo Taurus", "Moo", "Brown")
print(cow.sound)
print(cow.color)

polly = bird("Green")
polly.talk()
print(polly.color)

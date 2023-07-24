# My game needs to have a character with a name, health and magic points.
# It needs these values setup when it is initialized.
# It needs a method to output this data.

class Character:
    name = None
    health = None
    magic = None

    def __init__(self, name, health, magic):
        self.name = name
        self.health = health
        self.magic = magic

    def print_character(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nMagic: {self.magic}")


# There should be a sub-class 'player' which inherits from character and also has a number of lives.
# Player should also have an 'am I alive?' method which checks the player status and reports back yes or no.

def am_i_alive(lives):
    if lives <= 0:
        return "No"
    else:
        return "Yes"


class Player(Character):
    lives = None

    def __init__(self, lives, name, health, magic):
        super().__init__(name, health, magic)
        self.lives = lives

    def print_player(self):

        print(f"===PLAYER===\nName: {self.name}\nHealth: {self.health}\nMagic: {self.magic}\nLives: {self.lives}")


# There should also be an 'enemy' sub-class with additional 'type' and 'strength'.

class Enemy(Character):
    type_of_enemy = None
    strength = None

    def __init__(self, type_of_enemy, strength, name, health, magic):
        super().__init__(name, health, magic)
        self.type_of_enemy = type_of_enemy
        self.strength = strength


# 'enemy' should have two sub-classes:
# 'orc' with a 'speed' attribute.
# 'vampire' with a 'day/night' tracker

class Orc(Enemy):
    speed = None

    def __init__(self, speed, type_of_enemy, strength, name, health, magic):
        super().__init__(type_of_enemy, strength, name, health, magic)
        self.speed = speed

    def print_orc(self):
        print(f"===ORC===\nType of enemy: {self.type_of_enemy}\nName: {self.name}\nHealth: {self.health}\nMagic: {self.magic}\nSpeed: {self.speed}")


class Vampire(Enemy):
    day_night = None

    def __init__(self, day_night, type_of_enemy, strength, name, health, magic):
        super().__init__(type_of_enemy, strength, name, health, magic)
        self.day_night = day_night

    def print_vampire(self):
        print(f"===VAMPIRE===\nType of enemy: {self.type_of_enemy}\nName: {self.name}\nHealth: {self.health}\nMagic: {self.magic}\nDay or Night: {self.day_night}")


# Instantiate one player, two vampires and three orcs. You choose their names.
player_one = Player(3, "Joshua", 100, 50)
vampire_one = Vampire("day", "vampire", 80, "corina", 50, 60)
vampire_two = Vampire("night", "vampire", 30, "damon", 60, 80)
orc_one = Orc(70, "orc", 90, "orcon", 70, 40)
orc_two = Orc(90, "orc", 90, "Orcola", 40, 40)
orc_three = Orc(20, "orc", 30, "orcumber", 99, 99)

# Print out their values.
print(player_one.print_player())
print(vampire_one.print_vampire())
print(vampire_two.print_vampire())
print(orc_one.print_orc())
print(orc_two.print_orc())
print(orc_three.print_orc())


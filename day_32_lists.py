# python lists
# list = []
# challenge print random greetongs in other languages
import random as r
greetings = ["Bonjour","Hola", "Zdravstvuyte", "Nǐn hǎo", "Guten Tag", "Shalom"]
rnd_num = r.randint(0, len(greetings)-1)
print(f"{greetings[rnd_num]}")

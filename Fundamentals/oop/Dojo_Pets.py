import Ninja

    
matt = Ninja.Ninja("Matt", "Baldiwn", "Bones", "Kibble", "Cat", "Bo")
matt.feed().walk().bathe()
matt.feed()

print(matt.pet.health)
print(matt.pet.energy)
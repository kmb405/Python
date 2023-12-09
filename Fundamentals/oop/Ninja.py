import Pet

class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet, pet_name):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        if pet == "Dog":
            self.pet = Pet.Dog(name=pet_name, type=pet, tricks="Jump")
        elif pet == "Cat":
            self.pet = Pet.Cat(name=pet_name, type=pet, tricks="Fall")
        else:
            self.pet = Pet.Pet(name=pet_name, type=pet)

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self
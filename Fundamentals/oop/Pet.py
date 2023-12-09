class Pet:

    def __init__(self, name, type, sound="Whine"):
        self.name = name
        self.type = type
        self.health = 50
        self.energy = 50
        self.sound = sound

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        print(self.sound)
    
    

class Dog(Pet):

    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)

    def noise(self):
        print("Bark")


class Cat(Pet):

    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)

    def noise(self):
        print("Meow")
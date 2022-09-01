class Pet: 
    
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
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
        print(f"the {self.type} goes {self.sound}")
        return self 


class Ninja():
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"Walking {self.pet.name}")
        self.pet.play()
        return self

    def feed(self):
        print(f"Feeding {self.pet.name} {self.pet_food}")
        self.pet.eat()
    def bathe(self):
        print(f"Bathing {self.pet.name}")
        self.pet.noise()
    
joe = Pet("Joe","Fish", "swims","bubbles")

doug = Ninja("Doug","Dillon","shrimp","flakes", joe)

doug.feed()
doug.walk()
doug.bathe()
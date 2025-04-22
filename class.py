class Superhero:
    def __init__(self, name, alias, power, strength_level):
        self.name = name
        self.alias = alias
        self.power = power
        self.strength_level = strength_level

    def introduce(self):
        return f"I am {self.alias}, also known as {self.name}. My superpower is {self.power}!"

    def battle_cry(self):
        return f"{self.alias} is ready for battle!"


class FlyingHero(Superhero):
    def __init__(self, name, alias, power, strength_level, flight_speed):
        super().__init__(name, alias, power, strength_level)
        self.flight_speed = flight_speed
    
    def battle_cry(self):
        return f"{self.alias} takes to the skies at {self.flight_speed} mph!"


class SpeedsterHero(Superhero):
    def __init__(self, name, alias, power, strength_level, running_speed):
        super().__init__(name, alias, power, strength_level)
        self.running_speed = running_speed
    
    def battle_cry(self):
        return f"{self.alias} races ahead at {self.running_speed} mph!"


hero1 = FlyingHero("Ethan Sky", "Storm Hawk", "Aerokinesis", 85, 500)
hero2 = SpeedsterHero("Leano Blaze", "Flash Fury", "Super Speed", 90, 700)

print(hero1.introduce()) 
print(hero1.battle_cry()) 

print(hero2.introduce()) 
print(hero2.battle_cry())  

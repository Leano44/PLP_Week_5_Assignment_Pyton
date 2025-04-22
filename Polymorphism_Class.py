from abc import ABC, abstractmethod

# Abstract base class
class Mover(ABC):
    @abstractmethod
    def move(self):
        pass

# Car class
class Car(Mover):
    def move(self):
        return "Driving 🚗"

# Plane class
class Plane(Mover):
    def move(self):
        return "Flying ✈️"

# Animal class (Example: Cheetah)
class Cheetah(Mover):
    def move(self):
        return "Running 🏃‍♂️"

# Creating instances
vehicle1 = Car()
vehicle2 = Plane()
animal1 = Cheetah()

# Using polymorphism
for obj in [vehicle1, vehicle2, animal1]:
    print(obj.move())



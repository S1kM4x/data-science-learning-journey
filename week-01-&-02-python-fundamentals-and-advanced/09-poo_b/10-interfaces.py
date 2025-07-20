
from abc import ABC, abstractmethod

# Clase abstracta (obliga a utlizarla), si dentro del metodo no implementamos la parte abstracta, eso nos enviara errores constantes


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"

    def sleep(self):
        return "zzz.."


class Cat(Animal):
    def sound(self):
        return "Meow! Meow!"

    def sleep(self):
        return "zzz.."


taquito = Dog()
michifus = Cat()

print(taquito.sound())
print(taquito.sleep())
print(michifus.sound())
print(michifus.sleep())
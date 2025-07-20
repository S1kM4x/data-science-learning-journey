# Este metodo es para manejar informacion mas sensible e informacion que no debe ser verificada

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__password = "1234"  # name mangling _NOMBRECLASE__password
        # _Person__password

    def __generate_password(self):
        return f"$${self.name}{self.age}"


person1 = Person('Emilio', 28)
print(person1.name)
# print(person1.__password)
# print(person1.__generate_password())
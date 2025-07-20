
user = {
    'name': 'Emilio',
    'age': 28,
    'email': 'correavillarroel@gmail.com'
}

print(user) # {'name': 'Emilio','age': 28, 'email': 'correavillarroel@gmail.com'}

user1 = {
    'name': 'Emilio',
    'age': 28,
    'email': 'correavillarroel@gmail.com',
    (19.12, -89.23): 'Santiago de Chile' # Solamente ejemplo, como cordenadas.
}

user1['name'] = 'Emilio#1'
user1['age'] = 25
user1['country'] = 'Chile'

print(user1('name')) # Emilio#1
print(user1('age')) # 25
print(user1('country')) # Chile, cabe descatar que tambien podemos ir agregando palabras adicionales al diccionario, como este ejemplo.

# Los diccionarios no pueden ser mutables, podemos ocupar str, int y tuplas.
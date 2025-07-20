
user = {
    'name': 'Emilio',
    'age': 28,
    'greet': 'Hola Mundo',
    'numbers': [1, 2, 3]
}

# .get()
print(user.get('name')) # Emilio

# in
print(user.keys())
print(user.values())
print('name' in user) # True
print('Emilio' in user) # False, el problema aqui es que in solamente busca en las llaves y no en los valores
print('Emilio' in user.values()) # True, aqui si funciona ya que estamos buscando directamente en la seccion correspondiente
print('name' in user.keys())

print(user.items()) # Esta funcion ejecuta el diccionario completo.
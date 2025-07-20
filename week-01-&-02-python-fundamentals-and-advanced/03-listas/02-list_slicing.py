
shopping_cart = [
    'Camisas',
    'Zapatillas',
    'Calcetas',
    'Pantalones'
]

print(shopping_cart[0]) # Camisas
print(shopping_cart[1]) # Zapatillas
print(shopping_cart[2]) # Calcetas
print(shopping_cart[3]) # Pantalones

# [Inicio : fin]
new_list = shopping_cart[1:3]

new_list[0] = 'Zapatos'
new_list[1] = 'Collar'

print(new_list) # Crea una lista nueva
print(shopping_cart)

# Copiar una lista, ejercicio para copiar listas

new_cart = shopping_cart[:] # Si no se le incluyen numeros considerara todos los numeros
new_cart[0] = 'Playeras'
shopping_cart[1] = 'Zapatos'
print(shopping_cart)
print(new_cart)

# Corto Circuito

# OR
True or print('Hola Mundo') # el codigo no responte, esto es genrando el corto circuito, el codigo siempre busca un True, si lo cuenta en un comienzo esto se detiene.
False or print('Hola Mundo') # Hola Mundo

# AND
False and print('Hola Mundo') # Corto Circuito
True and print('Hola Mundo') # Hola Mundo

name = 'Emilio'
print(name and name.upper()) # Esta forma evita que el codigo se rompa si hay un None

# Recibas de forma dinamica nombre, year of birth, correo y password

'''
    Nombre: Emilio
    Email: correavillarroel@gmail.com
    Tendras 55 years en el 2050
    Tu password es: ****
'''

name = input('Cual es tu nomnbre? ')
year_of_birth = input('En que year naciste? ')
email = input('Cual es tu correo electronico? ')
password = input('Escribe tu password ')

future_age = 2050 - int(year_of_birth)
password_lenght = len(password)

card = f'''
    Nombre: {name}
    Email: {email}
    Tendras {future_age} years en el 2050
    Tu password es: {'*' * password_lenght}
'''

print(card)
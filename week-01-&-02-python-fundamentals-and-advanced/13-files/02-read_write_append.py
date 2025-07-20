
# Creamos y escribimos algo en el archivo primero
with open('test.txt', mode="r") as my_file:
    print(my_file.readlines())

# Ahora sí lo leemos
with open('archivo.txt', mode="w") as my_file:
    text = my_file.write(':)')

# Luego hacemos lectura/escritura
with open('test.txt', mode="r+") as my_file:
    print(my_file.readlines())
    text = my_file.write('Hola Mundo')

# Finalmente, modo append
with open('test.txt', mode="a") as my_file:
    text = my_file.write("123")
    print(text)

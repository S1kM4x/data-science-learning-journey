
my_file = open('test.txt')
# print(my_file.read()) # El interprete de python solamente lee una vez, las demas pondra un espacio
# print(my_file.read())
# print(my_file.read())

# seek
# my_file.seek(0) # Esta funcion sirve para leer dos veces el archivo dependiendo de donde queremos comenzar 
# print(my_file.read())

# Readline
print(my_file.readline()) # Esta funcion lee linea por linea
print(my_file.readline())
print(my_file.readline())

# Readlines
print(my_file.readlines()) # Esta funcion se encarga de leer el sobrante

my_file.close() # Esta funcion es obligatoria para poder cerrar el ciclo de lectura
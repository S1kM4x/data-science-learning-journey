
name = 'Emilio' # 0 E, 1 m, 2 i, 3 l, 4 i, 5 o. En programacion para realizar una cuenta se comienza desde cero.
# print(name) # Emilio

# print(name[0]) # E
# print(name[1]) # m
# print(name[2]) # i
# print(name[3]) # l 
# print(name[4]) # i
# print(name[5]) # o

# Luis name[3]

# Como obtener la ultima letra?
# print(name[-1]) # o

# [Start:Stop]
# Emilio
# Emi
# print(name[0:3]) # Tomar en consideracion que esta funcion no toma encuenta el ultimo numero, ejemplo considera 0,1,2.

# [Start:Stop:stepover]
# print(name[0:3:2]) # Ei

name_reverse = name[::-1]
print(name_reverse)
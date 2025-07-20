
# set1.symmetric_difference(set2), es funcion toma todos los valores que no estan en la interseccion
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference) # {1, 2, 5, 6}

# set1.issubset(set2) True o False, esta funcion analiza si los elementos de uno estan en el interior del otro, ejemplos abajo
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2)) # True
print(set2.issubset(set1)) # False

# set1.issuperset(set2), esta funcioan se encarga de saber si set 1, puede almacenar todos los datos de set 2, ejemplos abajo
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set1.issuperset(set2)) # True
print(set2.issuperset(set1)) # False
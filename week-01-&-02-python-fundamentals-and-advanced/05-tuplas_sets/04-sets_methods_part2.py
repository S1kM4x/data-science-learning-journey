
# set1.union(set2)
set1 = {1, 2, 3}
set2 = {4, 5, 6}

union_set = set1.union(set2)
print(union_set) # {1, 2, 3, 4, 5, 6}

# set1.intersection(set2)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)
print(intersection) # {3, 4}

# set1.difference(set2), esta funcion trae todo lo que es diferente de un set a otro, 
# por ejemplo toma el set 1 completo y analiza los datos y todo lo que es
# diferente a set 2 lo devuelve
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference1 = set1.difference(set2)
difference2 = set2.difference(set1)
print(difference1) # {1, 2} 
print(difference2) # {5, 6} 

numbers_list = [1, 2, 3, 4, 5]
print(numbers_list) # [1, 2, 3, 4, 5]

# pop() esta funcion remuve el ultimo numero de derecha a izquierda.
numbers_list.pop() # [1, 2, 3, 4]
numbers_list.pop([1]) # [1, 2, 3]
print(numbers_list)

# remove() esto remueve solamente un pieza del codigo.

numbers_list.remove(4)
print(numbers_list) # [1, 3]

# clear() esto elimina la lista completa
numbers_list.clear
print(numbers_list)

# Metodos de adicion

numbers_list = [1, 2, 3, 4, 5]
print(numbers_list)

#append
numbers_list.append(100) 
numbers_list.append(200)
print(numbers_list) # [1, 2, 3, 4, 5, 100, 200]

# Insert
numbers_list.insert(1, 200)
numbers_list.insert(3, 300) 

print(numbers_list) # [1, 200, 2, 300, 3, 4, 5, 100, 200]

# Extends
numbers_list.extend([11, 22, 33])

print(numbers_list) # [1, 200, 2, 300, 3, 4, 5, 100 ,200, 11, 22, 33]
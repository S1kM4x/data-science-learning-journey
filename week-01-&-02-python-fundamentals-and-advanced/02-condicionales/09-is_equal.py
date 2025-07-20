
# == Equal o igualdad

print(5 == 5) # True
print(True == 1) # True
print('' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True

new_list = []
other_list = []

# is compara en memoria "0x1234ab"
print(new_list is other_list)
print(new_list == other_list)
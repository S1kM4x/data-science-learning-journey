
letters = ['a', 'b', 'm', 'o', 'c', 'z,', 'g', 'd', 'e']
print(letters) # ['a', 'b', 'm', 'o', 'c', 'z,', 'g', 'd', 'e']

# sort(), esto ordena la lista por orden alfabetico.
letters.sort()
print(letters) # ['a', 'b', 'c', 'd', 'e', 'g', 'm', 'o', 'z,']

# sorted(), esto ordena la lista por orden alfabetico.
new_letters = sorted(letters)
print(new_letters) # ['a', 'b', 'c', 'd', 'e', 'g', 'm', 'o', 'z,']

new_letters = letters[:] # List Slicing
new_letters = letters.copy() # Este modofunciona igual que el de arriba pero mas largo y ocupa un poco mas recursos.
new_letters.sort()

# Reverse
letters.reverse()
print(letters) # ['z,', 'o', 'm', 'g', 'e', 'd', 'c', 'b', 'a']
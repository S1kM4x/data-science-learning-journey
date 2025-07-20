
# Truthy (Valores verdaderos)
print(bool(True))
print(bool(1))
print(bool(123))
print(bool(1.1))
print(bool(-1)) # Todo numero difernete a cero es verdadero
print(bool(1j))
print(bool('Hola'))
print(bool([1,2,3])) # Lista
print(bool((1,2,3))) # Tupla
print(bool({1,2,3})) # Set

# Falsey (Valores falsos)
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(''))
print(bool([])) # Lista
print(bool(())) # Tupla
print(bool({})) # Set
print(bool(None))
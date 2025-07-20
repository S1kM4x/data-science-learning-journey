
# Evaluar condiciones

# and (Va a pedir que todos los valores sean verdaderos)
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# or (Esta funcion pide que al menos uno de los valores sea verdadero)
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

# not (negar)
print(not True) # False
print(not False) # True

# and
age = 25
licensed = True

if age >= 18 and licensed:
    print('you can drive')
    
# or
is_student = False
membership = True

if is_student or membership:
    print("Obtain special price off")

# not
is_admin = False

if not is_admin:
    print('Denied acess')
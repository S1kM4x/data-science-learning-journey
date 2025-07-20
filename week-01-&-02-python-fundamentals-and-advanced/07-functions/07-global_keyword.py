
tax = 16


def change_global():
    global tax
    tax = 18
    return tax


print(tax) # 16

print(change_global()) # 18
print(tax) # 18 , para que la funcion actue debemos agregar la funcion global
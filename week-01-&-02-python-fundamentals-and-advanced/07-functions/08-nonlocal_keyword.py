
def outer():
    enclosing_variable = "Enclosing variable"

    def inner():
        nonlocal enclosing_variable
        enclosing_variable = "Enclosing Modificado"

    inner()
    print(enclosing_variable) # esta funcion ayuda a cambiar variables nonlocal, variables que estan fuera de la funcion inner


outer()
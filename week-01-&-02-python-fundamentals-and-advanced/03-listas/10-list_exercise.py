
# Crearás un carrito de compras que haga las siguientes funcionalidades:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito

print("Carrito de compras")
print("Opciones: ")
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Mostrar la lista ordenada")
print("4. Buscar producto")
print("5. Contar productos del carrito")
print("6. Vaciar el carrito")

shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]
option = input("Elige una opción (1-6): ")

if option == "1":
    product = input("Ingresa un nombre de producto: ")
    if product not in shopping_cart:
        shopping_cart.append(product)
        print("Producto agregado")
    else:
        print("El producto ya se encuentra en tu carrito")
elif option == "2":
    product = input("Ingresa un nombre de producto: ")
    if product in shopping_cart:
        shopping_cart.remove(product)
        print("Producto eliminado")
    else:
        print("El producto no está en la lista")
elif option == "3":
    if len(shopping_cart) > 0:
        print("Lista de compras: ")
        shopping_cart.sort()
        print(shopping_cart)
    else:
        print("La lista esta vacía")
elif option == "4":
    product = input("Ingresa un nombre de producto a buscar: ")
    if product in shopping_cart:
        print(f"{product} esta en la lista de compras")
    else:
        print("Producto no encontrado")
elif option == "5":
    print("Total de productos: ", len(shopping_cart))
elif option == "6":
    shopping_cart.clear()
    print("Lista vacia")
else:
    print("Opción no válida.")


print(shopping_cart)
    

# print("🛒 Carrito de compras")

# shopping_cart = ['Laptop', 'Vaso', 'Cafe', 'Audifonos']

# while True:
#     print("\nOpciones:")
#     print("1. Agregar producto")
#     print("2. Eliminar producto")
#     print("3. Mostrar la lista ordenada")
#     print("4. Buscar producto")
#     print("5. Contar productos del carrito")
#     print("6. Vaciar el carrito")
#     print("7. Salir")

#     option = input('Elije una opcion (1-7): ')

#     if option == '1':
#         producto = input("Ingresa el producto a agregar: ")
#         shopping_cart.append(producto)
#         print(f"✅ '{producto}' fue agregado al carrito.")

#     elif option == '2':
#         producto = input("Ingresa el producto a eliminar: ")
#         if producto in shopping_cart:
#             shopping_cart.remove(producto)
#             print(f"🗑️ '{producto}' fue eliminado del carrito.")
#         else:
#             print(f"❌ '{producto}' no está en el carrito.")

#     elif option == '3':
#         if shopping_cart:
#             print("📦 Lista ordenada del carrito:")
#             for item in sorted(shopping_cart):
#                 print(f"- {item}")
#         else:
#             print("🛒 El carrito está vacío.")

#     elif option == '4':
#         producto = input("Ingresa el producto a buscar: ")
#         if producto in shopping_cart:
#             print(f"🔎 '{producto}' sí está en el carrito.")
#         else:
#             print(f"❌ '{producto}' no se encuentra en el carrito.")

#     elif option == '5':
#         total = len(shopping_cart)
#         print(f"📊 Hay {total} producto(s) en el carrito.")

#     elif option == '6':
#         shopping_cart.clear()
#         print("🧹 El carrito ha sido vaciado.")

#     elif option == '7':
#         print("👋 Saliendo del programa. ¡Hasta luego!")
#         break

#     else:
#         print("❌ Opción no válida. Elije una opción del 1 al 7.")
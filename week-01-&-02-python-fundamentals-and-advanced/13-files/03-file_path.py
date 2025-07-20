
# Relative Path
# with open('fileFolder/relative.txt', mode="r") as my_file:
#     print(my_file.readlines())

with open('../Archivos/archivo.txt', mode="r") as my_file:
    print(my_file.readlines())

# Absolute Path
# Aquí meti la ruta en una variable para que no te de error la extensión
absolute_path = 'C:\Users\User\Documents\python\Archivos\archivo'
with open(absolute_path, mode="r") as my_file:
    print(my_file.readlines())
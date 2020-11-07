cadena1 = input("ingrese el nombre del padre: ")
cadena2 = input("ingrese el apellido del padre:")
cadena3 = input("digite su nombre: ")

dato1 = cadena1 + " " + cadena2

nombre_padre = dato1.split(cadena1 + " ")

nh1 = cadena3 + " " + nombre_padre[1]

cadena4 = input("ingrese el nombre de la madre: ")
cadena5 = input("ingrese el apellido del madre:")

dato2 = cadena4 + " " +cadena5

nombre_madre = dato2.split(cadena4 + " ")

nh2= nh1 + " " + nombre_madre[1]

nombreCompleto = nh2

print(nombreCompleto)







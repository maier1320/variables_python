#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    '''
    Realice un calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7
      
      '''
    # Ingresando datos por consola

    print("Seleccione 1-> +, 2-> -, 3-> *, 4-> /, 5 -> **")
    opcion = int(input("ingrese una opcion del 1 al 5: "))
    numero_1 = float(input("digite el primer valor numerico: "))
    numero_2 = float(input("digite el segundo valor numerico: "))

    # Condicionales
    if opcion == 1 or opcion <= 5:
            if opcion == 1:
                total = numero_1 + numero_2
                print(f"La suma entre {numero_1} y {numero_2} es {total:.2f}")
            elif opcion == 2:
                total = numero_1 - numero_2
                print(f"La resta entre {numero_1} y {numero_2} es {total:.2f}")
            elif opcion == 3:
                total = numero_1 * numero_2
                print(f"La multiplicación entre {numero_1} y {numero_2} es {total:.2f}")
            elif opcion == 4:
                total = numero_1 / numero_2
                print(f"La división entre {numero_1} y {numero_2} es {total:.2f}")
            elif opcion == 5:
                total = numero_1 ** numero_2
                print(f"La potencia de {numero_1} elevado a la {numero_2} es {total:.2f}")

def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona
    
    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''
    # Ingreso de datos por consola
    name = input("ingrese su nombre: ")
    surname = input("ingrese su apellido: ")
    dni = input("ingrese su número de documento: ")
    aged = input("ingrese su edad: ")
    height = input("ingrese su altura: ")

    nombres_completo = name + " " + surname

    print(f"Nombre Completo: {nombres_completo}, Dni {dni}")
    print(f"Nombre Completo: {nombres_completo}, Edad {aged} años, Altura {height}")

def ej3():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    
    # Ingreso de datos por consola
    cadena1 = input("ingrese el nombre del padre: ")
    cadena2 = input("ingrese el apellido del padre:")
    cadena3 = input("digite su nombre: ")

    dato1 = cadena1 + " " + cadena2

    nombre_padre = dato1.split(cadena1 + " ")

    nh1 = cadena3 + " " + nombre_padre[1]

    cadena4 = input("ingrese el nombre de la madre: ")
    cadena5 = input("ingrese el apellido del madre:")

    dato2 = cadena4 + " " + cadena5

    nombre_madre = dato2.split(cadena4 + " ")

    nh2 = nh1 + " " + nombre_madre[1]

    nombreCompleto = nh2

    print(nombreCompleto)

    """
def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')
    
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
"""


    cadena1 = input("ingrese el nombre de la persona1: ")
    cadena2 = input("ingrese el apellido de la persona1: ")

    dato1 = cadena1 + " " + cadena2

    cadena4 = input("ingrese el nombre de la persona2: ")
    cadena5 = input("ingrese el apellido del persona2:")

    dato1 = cadena4 + " " + cadena5

    np2 = dato1.split(cadena4 + " ")
    nombrePersona_2 = np2[1]

    #nh2 = nh1 + " " + nombre_madre[1]

    print(nombrePersona_2)



def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''


if __name__ == '__main__':
    print("Ejercicios de práctica")
#ej1()
#ej2()
#ej3()
ej4()
    # ej5()

"""
Funciones de uso general
1- print() imprime por consola el valor de una variable
2- input() leé lo que se digita en el teclado hasta que se presione la tecla enter y lo devuelve como texto
3- type() nos devuelve el tipo de dato de una variable
4- len() nos devuelve el largo de caracteres de un string

"""

variable = input("Ingresa un texto -->")
print("el contenido de la variable es",variable)
print("el tipo de la variable es",  type( variable )  )
logico = True
print("el tipo de la variable logico es",  type( logico )  )
entero = 100
print("el tipo de la variable entero es",  type( entero )  )
decimal = 3.14
print("el tipo de la variable decimal es",  type( decimal )  )
string = "Lenguaje de programación Python"
print("el tipo de la variable string es",  type( string )  )
print( "el largo del texto de la variable string es" , len ( string ) )

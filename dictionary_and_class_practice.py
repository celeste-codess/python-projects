#scribe un diccionario en Python que almacene el nombre de tres frutas como claves y su color como valor.
frutas = {"platano" : "amarillo",
          "manzana" : "roja",
          "durazno" : "naranja"}

##Escribe un diccionario en Python para almacenar el nombre y la edad de tres amigos.
amigos = {"Andrea" : 16,
          "Salvador" : 15,
          "Daira" : 12}


#ompleta el código para agregar una 
# nueva pareja clave-valor al diccionario '
# estudiante', donde la clave es 'edad' y el valor 17.
#estudiante["edad"] = 17

#Escribe una función en Python llamada 
# 'buscar_clave' que reciba un diccionario y una clave, y devuelva True si la clave existe en el diccionario o False si no.

def buscar_clave(diccionario, clave):
    return clave in diccionario
    
#Corrige el error en el siguiente código que 
# intenta acceder al valor de la clave 'telefono' en el diccionario 'contacto':

contacto = {'nombre': 'Ana', 'email': 'ana@example.com'}
print(contacto.get('telefono', 'None'))

"""Utilizas el nombre del diccionario, abres corchetes [] para poner el nombre de la clave que quieres cambiar,
y le asignas el nuevo valor usando el signo igual =
Ejemplo:

persona['edad'] = 25

 Para cambiar el valor de una clave en un diccionario, simplemente se asigna un nuevo valor a dicha clave.

"""

#Completa el siguiente código para agregar una nueva clave 'País' con valor 'España' al diccionario llamado persona:

persona = {'Nombre': 'Carlos', 'Edad': 19}
persona['País'] = 'España'

#Corrige el error en el siguiente código que causa que no se pueda modificar el valor de la clave 'edad' en el diccionario:

persona = {'nombre': 'Lucía', 'edad': 18}
persona['edad'] += 1

#recorra el diccionario  y muestre la frase: "Tengo X unidades de Y" para cada fruta.

frutas = {'manzana': 3, 'banana': 5, 'naranja': 2}
for fruta, cantidad in frutas.items():
    print(f"Tengo {cantidad} unidades de {fruta}")

 #Escribe un diccionario en Python llamado "estudiante"
 #  que contenga las siguientes claves y valores: nombre (cadena), edad (entero) y promedio (flotante).

estudiante = {"nombre" : "celeste",
              "edad" : 16,
              "promedio" : 9.5}

#Dado el diccionario siguiente: , escribe una línea de código para acceder y mostrar el valor de la clave "promedio".

alumno = {'nombre': 'Carlos', 'edad': 17, 'promedio': 9.0}
print(alumno.get("promedio"))

#Completa el siguiente código para agregar al diccionario "libro" la clave  con el valor .

libro = {'titulo': 'Cien años de soledad'}
libro["autor"] = "Gabriel García Márquez"
# Agrega aquí la clave y valor

#Escribe un fragmento de código que elimine la clave "promedio" del diccionario 

alumno = {'nombre': 'Laura', 'edad': 18, 'promedio': 9.2}
del alumno["promedio"]

# "persona" que contenga las claves "nombre" con tu nombre, "edad" con tu edad y "ciudad" con la ciudad donde vives.
persona = {"nombre" : "Celeste",
           "edad": 15,
           "cuidad": "Oaxaca"}

#todas las claves y valores del diccionario persona en líneas separadas, con el formato "clave: valor".
#Escribe un código que muestre todas las claves y valores del diccionario persona en líneas separadas, con el formato "clave: valor".

#Completa el código para agregar una clave  con el valor  al diccionario persona.

persona = {'nombre': 'Ana', 'edad': 18}
persona['email'] = 'ana@mail.com'

#scribe un diccionario llamado '' con las claves 'nombre', 'edad' y '' y asigna valores apropiados a cada una.
estudiante = {"nombre": "Celeste",
              "edad" : 16,
              "carrera" : "Mecatrónica"}

#
estudiante = {'nombre': 'Luis', 'edad': 16}
estudiante['promedio'] = 8.5

#Corrige el siguiente código para que imprima el valor asociado a la clave 'curso' del diccionario info:

info = {'curso': 'Python', 'duracion': 3}
print(info.get('curso'))

#'calificaciones' e imprima todas las claves y valores en formato ''.
estudiante = {"nombre" : "cleste",
              "edad" : 15,
              "curso" : "Español"}

#Dado el diccionario 
estudiantes = {"Ana": 15, "Luis": 18, "Maria": 17}

for valor, clave in estudiantes.items():
    print(f"{valor}: {clave}")


#escribe un pequeño código que imprima el nombre y la edad de cada estudiante usando un ciclo for.
#Escribe un diccionario en Python llamado "estudiante"

#  que tenga las siguientes claves y valores: nombre (string), edad (entero), y materias (lista de strings).
persona = {"nombre": "Celeste",
            "edad": 16,
            "ciudad": ""}


#Explica cómo accederías a la lista de materias del diccionario 
estudiante = {"nombre": "Lucía", "edad": 15, "materias": ["Biología", "Geografía"]} 

estudiante["materias"].append("Humanidades")


#primero acceder al valor "materias" de la clave estudiante y luego usando indexación 
print(estudiante["materias"][0])

#y cómo imprimirías la primera materia.

#buscar_edad" que reciba un diccionario con datos de una persona y devuelva la edad. Por ejemplo, para
#  , debe devolver 18.
dicc = {'nombre':'María', 'edad':18}

def buscar_edad(dicc):
    return dicc['edad']

#calcule la suma de valores en el diccionario

precios = {"manzana": 100, "naranja": 80}

suma = 0
for precio in precios.values():
    suma += precio

print(suma)



#Escribe un pequeño código que cree un diccionario contando cuántas veces aparece cada letra en la palabra "programa".
palabra = "programa"
dicc = {}

for letra in palabra:
    dicc[letra] = dicc.get(letra, 0) + 1

##scribe un diccionario en Python que almacene el nombre de tres frutas como claves y su color como valor.
#  Por ejemplo, manzana puede ser roja.
frutas = {"platano" : "amarillo",
          "manzana" : "roja",
          "durazno" : "naranja"}

frutas["platano"]
#Escribe un código que imprima todas las claves de un diccionario "notas" utilizando un bucle for.

for clave in "notas".keys():
    print(f"{clave}")

##Escribe un pequeño código en Python que recorra un diccionario frutas y muestre en pantalla todas las frutas y sus colores en el formato: .
estudiante = {"nombre": "Ana",
              "edad": 16,
              "curso": "programación"}

#y muestre por pantalla cada fruta junto con la cantidad.
inventario = {'manzanas': 5, 'peras': 3, 'naranjas': 2} 
for fruta, cantidad in inventario.items():
    print(f"{fruta}: {cantidad}")

###
###El método "get" se usa para obetener el valor de una clave dada, en dado caso de no existir no rompe el código dando error, aparece None o el mensaje que sea configurado
# es una colección de pares clave-valor con claves únicas y que sirve para acceder o almacenar información de forma rápida usando esas claves.
datos = {'a': 1, 'b': 2, 'c': 3}
for claves in datos:
    print(claves)           



##Una instancia de una clase con atributos y métodos específicos
# Un molde o plantilla que define las características y comportamientos de un objeto.
#Un tipo de dato que define las características y comportamientos de un objeto.
#Una instancia concreta de una clase con sus propios datos y  una clase es la plantilla o definición de un objeto que tiene metodos(acciones) y atributos(caracteristicas).
#Una instancia concreta con propiedades y métodos
#Un molde o plantilla que define las características(atributos) y comportamientos(métodos) de un objeto.
#se refiere a la instancia del objeto para acceder a sus atributos.'self' como la referencia a la instancia actual del objeto, que permite acceder y asignar sus atributos.

#"Persona" que tenga dos atributos: nombre y edad, 
# y un método que imprima un saludo con el nombre de la persona.
#Modifica la clase "Persona" que escribiste antes para agregar un método llamado "cumplir_anos" que aumente en 1 la edad de la persona.
#¿Cómo crearías un objeto de la clase "Persona" con el nombre "Ana" y la edad 18? Escribe el código en Python.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    def cumplir_anos(self):
        self.edad += 1 

persona1 = Persona("Ana", 18)

#Escribe un método llamado "pintar" que cambie el color del coche.
# estra solo el código del método dentro de la clase.

def pintar(self,nuevo_color):
    self.color = nuevo_color
    

#"Coche" en Python que tenga un atributo 
# "marca" y un método que 
# imprima "Este coche es de la marca: " seguido del nombre de la marca.
#"mi_coche" de la clase "Coche" con la marca "Toyota" y luego llamar al método que muestra la marca.

class Coche:
    def __init__(self, marca):
        self.marca = marca
    
    def mostrar_marca(self):
        print(f"Este coche es de la marca: {self.marca}")

mi_coche = Coche("Toyota")
mi_coche.mostrar_marca()

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

p = Persona('Ana')
print(p.nombre)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


#"Perro" que tenga un atributo llamado "nombre" y un método llamado "ladrar" que imprima "Guau!".
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Guau!")

mi_perro = Perro("Firulais")
mi_perro.ladrar

class Gato:
    def __init__(self, color):
        self.color = color

    def maullar(self):
        print("Miau!")

mi_gato = Gato("negro")
mi_gato.maullar()
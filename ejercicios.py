# # Crear una lista tupla y rango con numeros del uno al 10
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# rango = range(1, 10)

# print(lista, tupla, rango)

# # Andree - Sintaxis de diccionario
# persona = {
#   "nombre": "Pablo",
#   "apellido": "no se",
#   "edad": "desconocida"
# }
# print( persona["apellido"], persona["edad"], persona["nombre"])


# # Andree - Crea un conjunto

# un_set = set([1,2,3,4,5])
# otro_set = frozenset(un_set)
# print(un_set, otro_set)


# #Andree - f-strings
# nombref = 'Ana'
# lenguaje1 = 'Python'
# lenguaje2 = 'JavaScript'
# lenguaje3 = 'C++'
# print(f"Hola mi nombre es {nombref} y estoy aprendiendo {lenguaje1}, {lenguaje2} y {lenguaje3}")

#Condicionales

# respuesta = input("Ingresa un color:")
# if(respuesta == "amarillo"): 
#   print("Seleccionaste amarillo el color de la amistad")
# elif(respuesta == "rojo"):
#   print("Seleccionaste el color del amor")
# elif(respuesta == "verde"):
#   print("Elegiste el color de la esperanza")
# else: 
#   print("Sigue intentando")

# numero = 0
# suma = 0
# while numero <= 10:
#   if suma > 15:
#     break
#   if numero%2!=0:
#     numero += 1
#     suma +=numero
#     continue
#   numero += 1
#   print(suma)


# try:
#   numero = int(input("Ingrese un numero: "))
#   x = 10/numero
#   print(x)
# except ValueError:
#   print("Debes ingresar un valor valido")
# except ZeroDivisionError:
#   print("No se debe dividir un numero entre 0")

# try:
#   numero1 = int(input("Ingrese el primer numero: "))
#   numero2 = int(input("Ingrese el segundo numero: "))
#   resultado = numero1/numero2
#   print(resultado)
# except ZeroDivisionError:
#   print("No se debe dividir un numero entre 0")
# except Exception as e:
#   print("Error inesperado")
# finally:
#   print("El programa se completo")

# def numeros () :
#   a = int(input("Ingrese el primer numero: "))
#   b = int(input("Ingrese el segundo numero: "))
#   c = int(input("Ingrese el tercer numero: "))
#   print(a +b +c)
# numeros()

# def saludar(nombre = "Bebe", edad= 18):
#   print(f'Hola {nombre} ya se que tienes {edad}')
# saludar()
# "Andree", 20

# def saludar(*numeros):
#   lista = []
#   listacubo = []
#   for numero in numeros:
#     cuad = numero**2
#     lista.append(cuad)
#     cubo = numero**3
#     listacubo.append(cubo)
#   print(lista, listacubo)
# saludar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def mayor(a, b):
#   try:
#     if int(a) > int(b):
#       return a
#     elif int(b) > int(a):
#       return a
#   except ValueError:
#     return "Algo salio mal"  


# print(mayor(1,"jiji"))
# print(mayor(8, 4))
# print(mayor(2, 4))



# def funcion_externa ():
#   contador = 0
#   def funcion_interna ():
#     nonlocal contador
#     contador +=1
#     print(contador)
#   return funcion_interna
  

# mi_contador = funcion_externa()
# mi_contador()
# mi_contador()
# mi_contador()


# def externa(lista):
#   def interna(l):
#     suma = 0
#     for element in lista:
#       suma += element
#       print(suma)
#     print(suma)
#   interna(lista)
# externa([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# def contador ():
#   contador = 0
#   def contar ():
#     nonlocal contador
#     contador += 1
#     print(contador)
#   return contar
# mi_contador = contador()
# mi_contador()
# mi_contador()
# mi_contador()
# mi_contador()


# def lista (*lista):
#   # listas = lista
#   def elementos ():
#     # nonlocal listas
#     for element in lista:
#       print(element, lista.index(element))
#   return elementos()
# mi_lista = lista
# mi_lista(1,2,3,4,5,6,7,8,9,10)


# def suma(n):
#   if n == 0:
#     return 0
#   else:
#     return n + suma(n-1)
# print(suma(5))


# area = lambda r: 3.14*r**2
# print(area(2))
# print(area(3))
# print(area(4))
# print(area(5))


# for i in range(0, 21, 2):
#   print(i)


# def ocho (*lista):
#   def car ():
#     for element in lista:
#       if len(element) > 8:
#         print(element)
#   return car
# mi_ocho = ocho('uno', 'dioogggdnfg', '12345678')

# mi_ocho()


# def sumar_pares(lista):
#   sumar = 0
#   for element in lista:
#     if element %2 == 0:
#       cuadrado = element**2
#       sumar += cuadrado
#   return print(sumar)

# def sumar_impares(lista):
#   sumar_cubo = 0
#   for element in lista:
#     if element %2 != 0:
#       cubo = element**3
#       sumar_cubo += cubo
#   return print(sumar_cubo)


# def tercera(lista, sumar_pares, sumar_impares):
#   sumar_pares(lista)
#   sumar_impares(lista)

# tercera((1, 2, 3, 4, 5, 6, 7, 8, 9, 10) , sumar_pares, sumar_impares)

# texto = "este es el baile del michi, uno, dos, tres, cuatro"
# count = 0
# for char in texto:
#   count += 1
# print(count)

# def palabra (*lista): 
#   listafinal = []
#   for palabra in lista:
#     if(palabra.startswith('J')):
#       listafinal.append(palabra)
#   print(listafinal)
# palabra('Pablo', 'Jose', 'Juan', 'Andree')


# texto ="Este es un texto de ejemplo.\npython es un lenguaje de programación desafiante y poderoso."
# print(len(texto))

# lista = texto.split()
# print(lista)
# for i, element in enumerate(lista):
#   if element == "python":
#     lista[i] = element.capitalize()
# print(lista)

# Encuentra la posición de la primera aparición de la palabra 'desafiante'. 
# lista = texto.split()
# index= 0
# for i, element in enumerate(lista):
#   if element == "desafiante":
#     index = i 
# print(index, 'desafiante')

# Elimina espacios en blanco al principio y al final del texto.
# print(texto.strip(), 'strip')

# Divide el texto en una lista de palabras.
# lista = texto.split()
# print(lista, 'con split')

# Verifica si el texto comienza con la palabra 'Este'. 🧠
# print(texto.startswith('Este'))


# deportes = ['futbol', 'baloncesto', 'tenis', 'natacion']
# print(deportes[3])
# print(deportes[0:3])
# print(deportes[0:4])
# print(deportes[-2])


# juegos = ['monopoly', 'ajedrez', 'scrabble']
# mayusculas = [juego.upper()  for juego in juegos]
# print(mayusculas)

# num_letras = [len(juego) for juego in juegos]
# print(num_letras)

# lista del 1 al 30; for enumerate *3 fizz *5buzz Y 3y 5 fizzbuzz

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# resultado = []
# for element in lista:
#   resultado.append(element)
#   if element % 3 == 0 and element % 5 ==0:
#     resultado.append("fizz buzz")
#   elif element%3 == 0:
#     resultado.append("fizz")
#   elif element%5 == 0:
#     resultado.append("buzz")

# print(resultado)


# lista = ['platano', 'fresa', 'manzana']
# def funcion (frutas):
#   existe = False
#   lista = frutas
#   quitar = input("¿Qué fruta desea quitar: ")
#   print(quitar)
#   for element in lista:
#     if element == quitar:
#       lista.remove(element)
#       existe=True

#   if existe == True:
#     print('fruta eliminada',lista)
#   else:
#     print("La fruta que usted selecciono no se encuentra en la lista")
  
# funcion(["platano", "fresa", "manzana"])


# def Veces (lista, element):
#   count = 0
#   for elemento in lista:
#     if elemento == element:
#       count +=1
#   return print(count)

# Veces((1,2,3,4,5,6,1,2,3,1,2,6), 5)




# def crud ():
#   lista = ['Andree', 'Pablo', 'Tania', 'Diana']
#   operacion = int(input('Seleccione la operación que desea realizar (1-5) \n 1. Agregar Usuarios \n 2. Mostrar Usuarios \n 3. Actualizar Usuario \n 4. Borrar usuario \n 5. Salir\n'))
#   if(operacion == 1):
#     nuevo = input('Ingrese el usuario que desea agregar: ')
#     lista.append(nuevo)
#   elif(operacion == 2):
#     print(f'Los datos actuales son: {lista}')
#   elif(operacion == 3):
#     actual = input('Ingrese el dato actual: ')
#     modificar = input('Ingrese el dato modificado: ')
#     textoactual = lista.index(actual)
#     lista.remove(actual)
#     lista.insert(textoactual, modificar)
#   elif(operacion == 4):
#     aborrar= input('Ingrese el dato a borrar: ')
#     lista.remove(aborrar)
#   elif(operacion == 5):
#     return 
#   print(lista)
# crud()


# def Libros():
#   biblioteca_1= {'Harry Potter', 'Codigo da Vinci', 'El señor de los Anillos', 'Cien años de soledad'}
#   biblioteca_2= {'Harry Potter', 'Orgullo y Perjuicio', 'Cien años de Solead', 'Don Quijote'} 
#   print(biblioteca_1)
#   print(biblioteca_2)
#   print(f'Libros comunes de ambas bibliotecas {biblioteca_1.intersection(biblioteca_2)}')
#   print(f'Libros unicos en la biblioteca 1 {biblioteca_1.difference(biblioteca_2)}')
#   print(f'Libros unicos en la biblioteca 2 {biblioteca_2.difference(biblioteca_1)}')

#   print(f'Libros en la biblioteca completa son: {biblioteca_2.difference(biblioteca_1)}')

#   print(f'Libros unicos en la biblioteca 1 {biblioteca_1.union(biblioteca_2)}')

#   print(f'¿La biblioteca 1 es subconjunto de la biblioteca completa? {biblioteca_1.issubset(biblioteca_1.union(biblioteca_2))}')
  
#   nuevo = input('¿Cuál es el nuevo libro que desea agregar a la biblioteca: ')
#   print(f'El nuevo libro a sido añadido a ambas bibliotecas')
#   biblioteca_1.add(nuevo)
#   biblioteca_2.add(nuevo)
#   print(f'Libros unicos en la biblioteca 1 {biblioteca_1}')
#   print(f'Libros unicos en la biblioteca 2 {biblioteca_2}')

# Libros()


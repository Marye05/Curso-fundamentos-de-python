# Tuplas
#Estructura de datos inmutables que contiene una secuencia ordenada de elementos

Tupla = (1, 2, 3, 4)

numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')
print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD
# numbers.append(10)
print(numbers)
# numbers[1] = 'change'

print(strings)
print(strings.index('zule'))
print(strings.count('nico'))

my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

'''
Los elementos están separados por espacios luego de las comas
Puede contener cualquier tipo de datos
Cada posición de la tupla tiene un índice
Es inmutable y por lo tanto no puede ser modificada, lo que permite proteger mejor la data si no queremos que se modifique por error
Acceder a un elemento
Tupla = (”A”, “B”, “C”)

Tupla [0] Indice a consultar

“A” Nos retorna el resultado de la posición 0 en la tupla

Encontrar un elemento
Tupla = (”A”, “B”, “C”)

“A” in Tupla

True

“Z” in Tupla

False

Metodos
Buscar el Indice de un elemento

Tupla = (”A”, “B”, “C”)

Tupla.index(”A”)

0 Nos devuelve el indice del elemento que buscamos

Numero de veces que un elemento aparece en la Tupla

Tupla = (”A”, “B”, “C”)

Tupla.count(elemento)

Tupla.count(”B”)

1 Retorna el numero de veces del elemento en la Tupla
'''
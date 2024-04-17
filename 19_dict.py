my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': "bla bla bla",
  'name': 'Nicolas',
  'last_name': 'Molina Monroy',
  'age': 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))

print('avion' in my_dict)
print('otroqueno' in my_dict)

'''
Métodos de diccionario
Python tiene un conjunto de métodos integrados que puedes usar en diccionarios.

Method	Description
clear()	Elimina todos los elementos del diccionario.
copy()	Devuelve una copia del diccionario.
fromkeys()	Devuelve un diccionario con las claves y el valor especificados.
get()	Devuelve el valor de la clave especificada.
items()	Devuelve una lista que contiene una tupla para cada par clave-valor
keys()	Devuelve una lista que contiene las claves del diccionario.
pop()	Elimina el elemento con la clave especificada.
popitem()	Elimina el último par clave-valor insertado
setdefault()	Devuelve el valor de la clave especificada. Si la clave no existe: inserte la clave, con el valor especificado
update()	Actualiza el diccionario con los pares clave-valor especificados
values()	Devuelve una lista de todos los valores del diccionario.

'''


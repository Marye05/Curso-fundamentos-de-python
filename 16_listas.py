numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])
text = 'Hola'

# text[0] = 'W'

tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3])
print(True in types)
print('hola' in types)

# Listas
Lista = [1, 2, 3, 4, 5]

tasks = ['Hola', 'Hello']
print(tasks)

tasks[0] = 'Bye'
print(tasks)
# nueva lista sería así => ['Bye', 'Hello']
'''
Puede ser modificada
Cada elemento esta separado por una coma
Puede contener todo tipo de datos
Metodos para listas
Lista.metodo(indice,elemento) o

Lista.metodo(elemento)

Metodos importantes
.count(elemento) cuenta cuantas veces un elemento esta en una lista

.extend(lista) permite extender una lista agregándole los elementos de otra lista

.pop() elimina y retorna el ultimo elemento de la lista

.reverse() reversa el orden de la lista

.sort() ordena la lista de manera ascendente o descendente

Actualizar un valor

Lista = [1, 2, 3, 4, 5]

Lista[0] = -8

Lista = [-8, 2, 3, 4, 5], resultado de la lista luego de actualizar el valor

Agregar un elemento

Lista.append(indice,elemento) o

Lista.append(elemento) en este caso el nuevo elemento se agrega al final de la lista

Eliminar un elemento

Lista.remove(indice, elemento)
'''
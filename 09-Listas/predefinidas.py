cantantes = ['Arjona', 'Julio Iglesias', 'Madona', 'Facundo']
numeros = [1,2,5,8,3,4]


#Ordenar una lista

print(numeros)
numeros.sort()
print(numeros)

#Agregar elementos 

cantantes.append('Jose Luis Perales')
cantantes.insert(1, 'David Bisval')

print(cantantes)

#Eliminar elementos

cantantes.pop(1) # Por indice
cantantes.remove('Julio Iglesias')

print(cantantes)

#Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista

print('Arjona' in cantantes)

#Contar Elementos

print(len(cantantes))


#Cuantas veces aparece un elemento 

print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))

#Coneguir un indice
print('\n')
print(cantantes.index('Arjona'))

#Unir Listas

cantantes.extend(numeros)

print(cantantes)

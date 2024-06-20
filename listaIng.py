lista=[1,2,2,1,2,2,2,1,'Andres','Ingeniero de sistemas']
lista2=[1,3,4,2,5,6,8,7]

edad=input('Introduzca su edad: ')

print(lista)
lista.append(edad)
print(lista)
print(lista.count(2))#Cuandos 2 hay
print(lista.index('Andres'))#En que posicion esta lo recibido
lista2.sort()#Ordena ascendente
print(lista2)
lista2.reverse()#Ordena descendente
print(lista2)
lista2.remove(2)#Elimina el valor dado
print(lista2)
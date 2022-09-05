import random
import problema as P
print('¿Cuántas muestras?')
muestra = int(input())
#Crear un array de arboles en cuestion a las muestras
list = []
for n in range(muestra):
    arbol = P.tree()
    arbol.root = arbol.insertar(arbol.root, 0)
    list.append(arbol)
#Preguntar cuantas horas
print("Número de horas?")
horas = int(input())
arbol.creacion(list, horas)
for i in range(len(list)):
    temp = list[i]
    print("arbol "+ str(i+1))
    arbol.printI(temp.root)
 


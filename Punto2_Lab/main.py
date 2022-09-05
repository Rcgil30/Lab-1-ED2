import problema as P
print('¿Cuántas muestras?')
muestra = int(input())
#Crear un array de arboles en cuestion a las muestras
list = []
for n in range(muestra):
    arbol = P.tree()
    arbol.root = arbol.insertar(arbol.root, 0)
    list.append(arbol)
#print (list)
#for i in range(len(list)):
#    obj = list[n]
#    print (obj.root.nivel)
#Preguntar cuantas horas
print("Número de horas?")
#horas = int(input())
arbolin = P.tree()
arbolin.root = arbolin.insertar(arbolin.root, 0)
arbolin.root.izquierda= arbolin.paste(1)
arbolin.root.derecha=arbolin.paste(1)
arbolin.root.izquierda.izquierda = arbolin.paste(2)
liton = []
arbolin.guardanivel(3, arbolin.root, liton)
for i in range(len(liton)):
    temp= liton[i]
    print (temp.nivel)
arbolin.replicaciones(liton)
arbolin.printI(arbolin.root)
print("pausa")
hola = input()
for i in range(len(list)):
    for j in range(horas):
        lista = []
        #Guardar en una lista los virus activos de la hora anterior
        temp = list[i]
        arbol.guardanivel(j+1, temp.root, lista)      
        #A la lista empezar a insertar las replicas1
        arbol.replicaciones(lista)
     
for i in range(len(list)):
    temp = list[i]
    print(temp.root.nivel)
    print(temp.root.izquierda)
    print(temp.root.izquierda.izquierda)
    print(temp.root.izquierda.derecha)
    print(temp.root.derecha)
    print(temp.root.derecha.izquierda)
    print(temp.root.derecha.derecha)
 


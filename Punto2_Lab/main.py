import random
import problema as P
print('¿Cuántas muestras?')
muestra = int(input())
while muestra>=10:
    print("No recomendamos usar más de 9 muestras, digita de nuevo")
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
#Validación
while horas>=21:
    print("Debido a los recursos no está permitido superar las 20 horas, digita de nuevo")
    horas = int(input())
arbol.creacion(list, horas)
menu = 0
while menu != 6:
    print("¿Que deseas hacer con las muestras?")
    print("[1]Número de replicaciones totales por muestra")
    print("[2]Cantidad de replicas con mutaciones fertiles")
    print("[3]Cantidad de replicas con mutaciones infertiles")
    print("[4]replicas del virus vivas")
    print("[5]Impresión de muestras")
    print("[6]Salir")
    menu = int(input())
    #Validación
    while menu<1 or menu>6:
        print("Opciones no validas, digitas de nuevo")
        menu = int(input())
    if menu == 1:
        #Para cada muestra conseguir una lista de todos sus nodos y así ver su cantidad restandole la raíz
        for i in range(len(list)):
            tree = list[i]
            lista =[]
            arbol.cantidad(tree.root, lista)
            print("Número de replicaciones para la muestra " + str(i+1)+ ": "+ str(len(lista)-1))
    if menu == 2:
        #para cada muestra busca los fertiles y los almacena en una lista
        for i in range(len(list)):
            tree = list[i]
            lista =[]
            arbol.fertiles(tree.root, lista)
            print("Número de replicaciones fertiles para la muestra " + str(i+1)+ ": "+ str(len(lista)))
    if menu == 3:
        #para cada muestra busca los infertiles y los almacena en una lista
        for i in range(len(list)):
            tree = list[i]
            lista =[]
            arbol.infertiles(tree.root, lista)
            print("Número de replicaciones infertiles para la muestra " + str(i+1)+ ": "+ str(len(lista)))
    if menu == 4:
        #Busca las hojas de cada muestra
        for i in range(len(list)):
            tree = list[i]
            lista =[]
            arbol.vivos(tree.root, lista)
            print("Número de replicas del virus vivas para la muestra " + str(i+1)+ ": "+ str(len(lista)))
    if menu == 5:
        #Pregunta de validación
        print("La impresión de las muestras será a traves de inorden, si el número de horas es muy alto será dificil de visualizar")
        print("¿Deseas imprimir las muestras?[1]Si [2]No")
        decision= int(input())
        while decision<1 or decision>2:
            print("Respuesta no valida, digita de nuevo")
            decision= int(input())
        if decision ==1:
            for i in range(len(list)):
                tree = list[i]
                print("Muestra número "+str(i+1)+":")
                arbol.printI(tree.root)
    if menu == 6:
        print("Vuelva pronto")

 


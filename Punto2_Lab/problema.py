import random
class Node():
    def __init__(self, dato) -> None:
        self.nivel = dato
        self.infertilidad = 0
        self.Fertilidad = 0
        self.izquierda: Node = None
        self.derecha: Node = None
class tree():
    def __init__(self) -> None:
        self.root: Node = None
    def insertar (self, root:Node, dato:int):
        if root is None:
            return Node(dato)
    def guardanivel (self, nivel: int, Nodo: Node, lista: list):
        if Nodo is None:
            return
        #En una busqueda de inorden se buscan los elementos que su nivel corresponda a la ultima hora y los guarda en una lista
        if (Nodo.nivel == (nivel-1)):
            lista.append(Nodo)
        self.guardanivel (nivel, Nodo.izquierda, lista)
        self.guardanivel(nivel, Nodo.derecha, lista)   
    def creacion ( self, muestras:list, horas:int):
        for i in range(len(muestras)):
            #Se toma el arbol correspondiente
            arbol = muestras[i]
            for j in range(horas):
                #Para cada hora hacer las replicaciones
                nivhora = []
                self.guardanivel( j+1,arbol.root, nivhora)
                for k in range(len(nivhora)):
                    nodo = nivhora[k]
                    if nodo.nivel == 0:
                        #Garantizar el hijo de la izquierda
                        nodo.izquierda = Node(nodo.nivel + 1)
                        #infertilidad
                        if random.uniform(0, 1) <= 0.03:
                            nodo.izquierda.infertilidad = 1
                        else:
                            if random.uniform(0, 1) <= 0.01:
                                nodo.izquierda.Fertilidad = 1
                        #Comprobar hijo derecha
                        if random.uniform(0, 1)<=0.8:
                            nodo.derecha = Node(nodo.nivel +1)
                            #Calculo de fertilidad e infertilidad
                            if random.uniform(0, 1)<= 0.03:
                                nodo.derecha.infertilidad = 1
                            else:
                                if random.uniform(0, 1)<= 0.01:
                                    nodo.derecha.Fertilidad = 1
                    else:
                        if nodo.infertilidad !=1:
                            #Hijo izquierda
                            if nodo.Fertilidad == 1:
                                nodo.izquierda = Node(nodo.nivel +1)
                                #infertilidad
                                if random.uniform(0, 1) <= 0.03:
                                    nodo.izquierda.infertilidad = 1
                                else:
                                    if random.uniform(0, 1) <= 0.01:
                                        nodo.izquierda.Fertilidad = 1
                            else:
                                if random.uniform(0, 1)<=0.8:
                                    nodo.izquierda = Node(nodo.nivel +1)
                                    #infertilidad
                                    if random.uniform(0, 1) <= 0.03:
                                        nodo.izquierda.infertilidad = 1
                                    else:
                                        if random.uniform(0, 1) <= 0.01:
                                            nodo.izquierda.Fertilidad = 1
                            #Hijo derecha
                            if nodo.Fertilidad == 1:
                                nodo.derecha = Node(nodo.nivel +1)
                                #infertilidad
                                if random.uniform(0, 1) <= 0.03:
                                    nodo.derecha.infertilidad = 1
                                else:
                                    if random.uniform(0, 1) <= 0.01:
                                        nodo.derecha.Fertilidad = 1
                            else:
                                if random.uniform(0, 1)<=0.8:
                                    nodo.derecha = Node(nodo.nivel +1)
                                    #infertilidad
                                    if random.uniform(0, 1) <= 0.03:
                                        nodo.derecha.infertilidad = 1
                                    else:
                                        if random.uniform(0, 1) <= 0.01:
                                            nodo.derecha.Fertilidad = 1
                    nivhora[k]=nodo
    def printI (self, Nodo:Node):
        #Impresion en inorden
        if Nodo is None:
            return
        print (str(Nodo.nivel) +" ")
        self.printI(Nodo.izquierda)
        self.printI(Nodo.derecha)
    def cantidad(self, Nodo:Node, num:list):
        if Nodo is None:
            return
        #Guarda todos los elementos en una lista
        num.append(Nodo)
        self.cantidad(Nodo.izquierda, num)
        self.cantidad(Nodo.derecha, num)
    def fertiles(self, Nodo:Node, num: list):
        if Nodo is None:
            return
        #Si es fertil se guarda en una lista
        if Nodo.Fertilidad ==1:
            num.append(Nodo)
        self.fertiles(Nodo.izquierda, num)
        self.fertiles(Nodo.derecha, num)
    def infertiles(self, Nodo:Node, num: list):
        if Nodo is None:
            return
        #Si es infertil se guarda en una lista
        if Nodo.infertilidad ==1:
            num.append(Nodo)
        self.infertiles(Nodo.izquierda, num)
        self.infertiles(Nodo.derecha, num)
    def isLeaf(self, node:Node):
        #retorna verdadero si es una hora, es decir si no tiene hijos
        return node.izquierda is None and node.derecha is None
    def vivos(self, Nodo:Node, num: list):
        if Nodo is None:
            return
        #Si el nodo es una hoja lo guarda en una lista
        if self.isLeaf(Nodo):
            num.append(Nodo)
        self.vivos(Nodo.izquierda, num)
        self.vivos(Nodo.derecha, num)
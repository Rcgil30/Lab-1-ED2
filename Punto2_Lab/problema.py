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
    def paste (self, dato):
        return Node(dato)

    def insertar (self, root:Node, dato:int):
        if root is None:
            return Node(dato)


    def guardanivel (self, nivel: int, Nodo: Node, lista: list):
        if Nodo is None:
            return
        if (Nodo.nivel == (nivel-1)):
            lista.append(Nodo)
        self.guardanivel (nivel, Nodo.izquierda, lista)
        self.guardanivel(nivel, Nodo.derecha, lista)


    def replicaciones (self, muestras: list):
        for i in range(len(muestras)):
            temp = muestras[i]
            if temp.nivel == 0:
                #Garantizar el hijo de la izquierda
                temp.izquierda = Node(temp.nivel+1)
                #Infertilidad
                infertil = random.uniform(0, 1)
                if infertil<= 0.3:
                    #Es infertil
                    temp.izquierda.infertilidad = 1
                else: 
                    #Calcular Fertilidad segura
                    fertil = random.uniform(0, 1)
                    if fertil <= 0.1:
                        #Es fertil
                        temp.izquierda.Fertilidad= 1
                #Calcular la reproducción del hijo de la derecha
                rep = random.uniform(0, 1)
                if rep<= 0.4:
                    #Hay hijo
                    temp.derecha = Node(temp.nivel+1)
                    #Calculo de la infertilidad
                    infertil = random.uniform(0, 1)
                    if infertil<= 0.3:
                        temp.derecha.infertilidad = 1
                    else: 
                        #Calculo de fertilidad segura
                        fertil = random.uniform(0, 1)
                        if fertil <= 0.1:
                            temp.derecha.Fertilidad= 1
            else:
                #Para los otros niveles.
                if temp.infertilidad != 1:
                    if temp.Fertilidad == 1:
                        temp.izquierda = Node(temp.nivel+1)
                        temp.derecha = Node(temp.nivel+1)
                    else:
                        #Calcular iz
                        rep = random.uniform(0, 1)
                        if rep<= 0.4:
                            temp.izquierda = Node(temp.nivel+1)
                        #Calcular derecha
                        rep = random.uniform(0, 1)
                        if rep<= 0.4:
                            temp.derecha = Node(temp.nivel+1)
                    #Calcular las mutaciones
                    if temp.izquierda != None:
                        infertil = random.uniform(0, 1)
                        if infertil<= 0.3:
                            #Es infertil
                            temp.izquierda.infertilidad = 1
                        else: 
                            #Calcular Fertilidad segura
                            fertil = random.uniform(0, 1)
                            if fertil <= 0.1:
                                #Es fertil
                                temp.izquierda.Fertilidad= 1
                    if temp.derecha != None:
                        infertil = random.uniform(0, 1)
                        if infertil<= 0.3:
                            temp.derecha.infertilidad = 1
                        else: 
                            #Calculo de fertilidad segura
                            fertil = random.uniform(0, 1)
                            if fertil <= 0.1:
                                temp.derecha.Fertilidad= 1
    def printI (self, Nodo:Node):
        if Nodo is None:
            return
        print (str(Nodo.nivel) +" ")
        self.printI(Nodo.izquierda)
        self.printI(Nodo.derecha)
        
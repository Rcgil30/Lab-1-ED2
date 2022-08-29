#GUI de python que utilizaremos para la interfaz
import tkinter as tk
#Esta librería nos permite cambiar el tipo de fuente en los label y botones
import tkinter.font as tkFont
# PARA CREAR LA INTERFAZ GRÁFICA
# Creamos la ventana principal
ventana = tk.Tk()
# Tamaño de la ventana:
Height = 918
Width = 520
ventana.geometry("918x520+230+100")  # para el tamaño y centrado de la interfaz
# Título de la ventana principal
ventana.title("Punto 1, laboratorio #1")
# Esto sirve para que el usuario no pueda agrandar la pantalla, ya que
# de lo contrario, se distorciona la interfaz
ventana.resizable(width=0, height=0)
# Creamos un Tipo de letra para colocarselo a los botones en las pantallas
Fuente_principal = tkFont.Font(family="Lucida Bright", size=11)
# Tipo de letra de la disponibilidad en los label
#Creamos una clase nodo, nuestro constructor
class Node:
    def __init__(self, data) -> None:
        self.data = data #Dato del nodo
        self.left: Node = None  #Enlace izquierdo del nodo
        self.right: Node = None #Enlace derecho del nodo
        self.level = 0  #Nivel del nodo

    def __repr__(self) -> str:
        return f"data: {self.data}"

#En esta clase se encuentra todo lo relacionado a las forma de recorrido del nodo
class Tree():
    def __init__(self) -> None:
        self.root: Node = None
    
    def BuscarNodo(self, root: Node, data):
        """Función para buscar un nodo según su dato y retornar el nodo si lo encuentra"""
        if root is None:
            return None
        if root.data == data:
            return root
        if data > root.data:
            return self.BuscarNodo(root.right, data)
        else: 
            return self.BuscarNodo(root.left, data)

    def insert(self, data):
        """Función para insertar un nodo"""
        if self.root is None:
            self.root = Node(data)
        elif self.BuscarNodo(self.root, data) is not None:
            print("Nodo ya se encuentra en el árbol")
        else:
            self.root = self._insert_(self.root, data)

    #Insertar un nodo en un árbol
    def _insert_(self, root: Node, data):
        #Si la raíz es nula entonces me retorna el dato del nodo
        if root is None:  
            return Node(data) 
        #Como la idea es insertar un nodo en un AVL, debemos usar su concepto de busqueda
        elif data < root.data: #Si el dato del nodo que queremos insertar es menor a el nodo en el que estamos
            #Nos movemos al lado izquierdo, llamando a la función de nuevo (recursividad) hasta  quedar en nulo
            #y que el condicional de arriba lo inserte
            root.left = self._insert_(root.left, data) 
        else:#Lo mimso con el lado derecho            
            root.right = self._insert_(root.right, data)

        self.CalculateLevel() #calculamos el nivel cada vez que pasados de nodo en nodo para ver si hay un desbalance
        
        #Calculamos el balance a cada uno de nuestros nodos.
        balance = self.Balance(root)
        if ((balance < -1) and data < root.left.data):
            return self.RotacionIzquierda(root)
        if (balance > 1 and data > root.right.data):
            return self.RotacionDerecha(root)
        if (balance < -1 and data > root.left.data):
            root.left = self.RotacionDerecha(root.left)
            return self.RotacionIzquierda(root)
        if (balance > 1 and data < root.right.data):
            root.right = self.RotacionIzquierda(root.right)
            return self.RotacionDerecha(root)

        return root

    def delete(self, data):
        if self.BuscarNodo(self.root, data) is None:
            print("Nodo no encontrado")
        else:
            self.root = self._delete_(self.root, data)

    def _delete_(self, root: Node, data):
        if root is None:
            return root
        elif data < root.data:
            root.left = self._delete_(root.left, data)
        elif data > root.data:
            root.right = self._delete_(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self._delete_(root.right, temp.data)
        
        if root is None: 
            return root
        self.CalculateLevel()
        balance = self.Balance(root)
        if balance > 1 and self.Balance(root.left) >= 0:
            return self.RotacionDerecha(root)
 
        if balance < -1 and self.Balance(root.right) <= 0:
            return self.RotacionIzquierda(root)
 
        if balance > 1 and self.Balance(root.left) < 0:
            root.left = self.RotacionIzquierda(root.left)
            return self.RotacionDerecha(root)
 
        if balance < -1 and self.Balance(root.right) > 0:
            root.right = self.RotacionDerecha(root.right)
            return self.RotacionIzquierda(root)

        return root

    def getMinValueNode(self, root: Node) -> Node:
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)


    def CalculateLevel(self): #Para calcular el nivel del nodo en el que nos encontramos, se hace un recorrido por nivel
        if self.root.level != 0:
            self.root.level = 0
        node = self.root 
        s = [node] #Creamos una lista q tiene como objeto el nuestro nodo
        while len(s) > 0: #mientras que el tamaño de nuestra lista sea mayor a 0
            node = s.pop(0) #quitamos de la lista el nodo en el que estamos
            if node.left is not None: #mientras que haya un nodo a la izquierda
                s.append(node.left)  #agregamos a la lista el nodo a la izquierda
                node.left.level = node.level + 1 #Se le suma 1 al nivel cada vez que pase al siguiente
            if node.right is not None: #Se realiza el mismo proceso con el derecho
                s.append(node.right)
                node.right.level = node.level + 1

    #Esta función me retorna el nivel del nodo que se encuentras mas abajo, esto se utiliza para calcular el balance
    def BuscarMax(self, root: Node):
        if root is None: #si no hay nodo entonces el nivel es 0
            return 0
        node = root 
        s = [node] #Creamos una lista q tiene como objeto el nuestro nodo
        while len(s) > 0: 
            node = s.pop(0)
            if node.left is not None:
                s.append(node.left)
            if node.right is not None:
                s.append(node.right)
        return node.level

    def Balance(self, root: Node):
        if root is None:
            return 0
        rheight = self.BuscarMax(root.right) 
        lheight = self.BuscarMax(root.left) 
        if (rheight != 0):
            rheight -= root.level
        if (lheight != 0):
            lheight -= root.level
        return rheight - lheight
    
    def RotacionIzquierda(self, root: Node): #Para balancearlo 
        child = root.left
        root.left = child.right
        child.right = root
        self.CalculateLevel()
        return child

    def RotacionDerecha(self, root: Node):
        child = root.right
        root.right = child.left
        child.left = root
        self.CalculateLevel()
        return child

    def preorder(self, root: Node):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def AlturaNodo(self, root:Node):
        temp = self.BuscarMax(root)
        return temp - root.level

    def EncontrarAbuelo(self, root:Node, data):
        if root is None or root.data == data:
            return None
        if root.left is not None:
            if root.left.left is not None:
                if root.left.left.data == data:
                    return root
            if root.left.right is not None:
                if root.left.right.data == data:
                    return root
        
        if root.right is not None:
            if root.right.left is not None:
                if root.right.left.data == data:
                    return root
            if root.right.right is not None:
                if root.right.right.data == data:
                    return root
        if(data > root.data):
            self.EncontrarAbuelo(root.right, data)
        else:
            self.EncontrarAbuelo(root.left, data)

    def EncontrarTio(self, data):
        abuelo = self.EncontrarAbuelo(self.root, data)
        if abuelo is None:
            return None
        if data > abuelo.data:
            return abuelo.left
        return abuelo.right
    
    def LevelTraversal(self):
        self.CalculateLevel()
        h = self.AlturaNodo(self.root)
        for i in range(1, h+2):
            self.CurrentLevel(self.root, i)

    def CurrentLevel(self, root: Node, level):
        if root is None:
            return
        if level == 1:
            print(root.data, end=" ")
        elif level > 1:
            self.CurrentLevel(root.left , level-1)
            self.CurrentLevel(root.right , level-1)

#Objeto de la clase tree
tree = Tree()
#Creamos manualamente nuestro árbol con el que probaremos insertar nodos
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)
tree.preorder(tree.root) 
print()
tree.LevelTraversal()

# El mainloop lleva el registro de todo lo que está sucediendo en la ventana:
ventana.mainloop()

abuelo = tree.EncontrarAbuelo(tree.root, 10)
tio = tree.EncontrarTio(50)
#print(f"{abuelo} y {tio}")
nodo = tree.BuscarNodo(tree.root, 40)
#print(nodo)

tree2 = Tree()
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for num in nums:
    tree2.insert(num)
#tree2.preorder(tree2.root)
tree2.delete(10)
#print()
#tree2.preorder(tree2.root)

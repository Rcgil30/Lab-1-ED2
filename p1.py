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
    def __init__(self, data: int) -> None:
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
    
    def BuscarNodo(self, root: Node, data: int):
        """Función para buscar un nodo según su dato y retornar el nodo si lo encuentra"""
        if root is None:
            return None
        if root.data == data:
            return root
        if data > root.data:
            return self.BuscarNodo(root.right, data)
        else: 
            return self.BuscarNodo(root.left, data)

    def insert(self, data: int):
        """Función para insertar un nodo"""
        if self.root is None: #Si no hay raíz, se crea un nuevo nodo y se le asigna
            self.root = Node(data)
        elif self.BuscarNodo(self.root, data) is not None: #Validación de que el nodo no exista previamente
            print("Nodo ya se encuentra en el árbol")
        else:
            self.root = self._insert_(self.root, data) #Si ningúno de los otros casos se da, llamamos esta función para 
                                                       #insertar un nuevo nodo y rebalancear según sea necesario

    #Insertar un nodo en un árbol
    #Función privada que inserta un nodo en un árbol
    def _insert_(self, root: Node, data: int):
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

    def delete(self, data: int):
        """Función para borrar un nodo"""
        if self.BuscarNodo(self.root, data) is None:
            print("Nodo no encontrado")
        else:
            self.root = self._delete_(self.root, data)

    def _delete_(self, root: Node, data: int):
        if root is None: #Validación de que no llegemos a un nodo nulo y que cause error
            return root
        #Nos movemos en el árbol de forma recursiva aprovechando las propiedades de los ABB
        elif data < root.data:
            root.left = self._delete_(root.left, data)
        elif data > root.data:
            root.right = self._delete_(root.right, data)
        else: #Cuando encuentra el dato a borrar
            #Si alguno de los hijos es nulo, el otro intercambia lugares con el padre y se borra el padre
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            #Si ambos hijos existen, se cambia el dato a borrar con el mínimo valor en el subárbol derecho,
            #para luego borrar nuevamente
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            # Después de este llamado, se debería llegar a alguno de los casos que se presentan en los condicionales
            #previamente explicados, a partir de lo cual se realizan las validaciones del balance
            root.right = self._delete_(root.right, temp.data)
            
        #Si el nodo es nulo volvemos al paso anterior en espera
        if root is None: 
            return root
        #Recalculamos el nivel de cada nodo y sacamos el balance de la raíz
        self.CalculateLevel() 
        balance = self.Balance(root)
        #Si hay un desbalance a la izquierda y el nodo izquierdo tiene un balance distino de 1
        if balance < -1 and self.Balance(root.left) <= 0:
            #Rotación simple izquierda
            return self.RotacionIzquierda(root)
        #Si hay un desbalance a la derecha y el nodo derecho tiene un balance distino de -1
        if balance > 1 and self.Balance(root.right) >= 0:
            #Rotación simple derecha
            return self.RotacionDerecha(root)
        #Si hay un desbalance a la izquierda y el nodo izquierdo tiene un balance igual a 1
        if balance < -1 and self.Balance(root.left) > 0:
            #Rotación doble izquierda
            root.left = self.RotacionDerecha(root.left)
            return self.RotacionIzquierda(root)
        #Si hay un desbalance a la derecha y el nodo derecho tiene un balance igual a -1
        if balance > 1 and self.Balance(root.right) < 0:
            #Rotación doble derecha
            root.right = self.RotacionIzquierda(root.left)
            return self.RotacionDerecha(root)
        # Si el nodo no tiene desbalances, se retorna para seguir con los nodos antecesores
        return root

    def getMinValueNode(self, root: Node) -> Node:
        """Función que devuelve el nodo de menor valor a partir de cualquier nodo"""
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)



    def CalculateLevel(self): #Para calcular el nivel del nodo en el que nos encontramos, se hace un recorrido por nivel
        """Función que calcula el nivel de todos los nodos"""
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
        """Función que encuentra el nivel más bajo en el árbol a partir de cualquier nodo"""
        if root is None: #si no hay nodo entonces el nivel es 0
            return 0
        node = root 
        s = [node] #Creamos una lista q tiene como objeto el nuestro nodo
        while len(s) > 0:  #mientras que la lista no esté vacía 
            node = s.pop(0) #sacamos el nodo de la lista
            if node.left is not None: #Si tiene hijo a la izquierda
                s.append(node.left)  #ingresamos cada nodo
            if node.right is not None: #si tiene hijos a la derecha
                s.append(node.right) #ingresamos cada nodo
        return node.level #obtenemos el nivel del nodo

    def Balance(self, root: Node):
        """Función para obtener el balance de cada nodo""" 
        rheight = self.BuscarMax(root.right) #buscamos balance del hijo derecho
        lheight = self.BuscarMax(root.left)  #buscamos balance del hijo izquierdo
        if (rheight != 0): 
            rheight -= root.level
        if (lheight != 0):
            lheight -= root.level
        return rheight - lheight
    
    def RotacionIzquierda(self, root: Node): 
        """Rotación simple izquierda"""
        child = root.left #hijo recibe nodo izquierdo
        root.left = child.right #nodo izquierdo recibe hijo derecho
        child.right = root #hijo derecho recibe nodo
        self.CalculateLevel() #recalculamos el nivel de cada uno de los nodos
        return child 

    def RotacionDerecha(self, root: Node): 
        """Rotación simple derecha"""
        child = root.right
        root.right = child.left
        child.left = root
        self.CalculateLevel()
        return child

    def preorder(self, root: Node): 
        """Recorrido recursivo en order traversal"""
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def AlturaNodo(self, root:Node):
        """Función que devuelve la altura de un nodo (Entiendase como el 
        número de aristas más larga desde el nodo hasta un nodo hoja)"""
        temp = self.BuscarMax(root)
        return temp - root.level

    def EncontrarAbuelo(self, root:Node, data: int):
        """Función para encontrar el abuelo de un nodo dado el dato"""
        if root is None or root.data == data: #Si el nodo es nulo o tiene el dato a buscar, el abuelo no existe
            return None
        if root.left is not None: #Validación para no incurrir en NullPointer
            if root.left.left is not None:
                if root.left.left.data == data: 
                    return root #Si encontramos el dato en alguno de los nietos, devolvemos el nodo 
            if root.left.right is not None:
                if root.left.right.data == data:
                    return root
        
        if root.right is not None: #Mismas validaciones para el subárbol derecho
            if root.right.left is not None:
                if root.right.left.data == data:
                    return root
            if root.right.right is not None:
                if root.right.right.data == data:
                    return root
        if(data > root.data): #Si no encontramos el nodo, nos movemos en el árbol llamando el método nuevamente
            self.EncontrarAbuelo(root.right, data)
        else:
            self.EncontrarAbuelo(root.left, data)

    def EncontrarTio(self, data: int):
        """Función para encontrar el abuelo de un nodo dado el dato"""
        abuelo = self.EncontrarAbuelo(self.root, data) #Ecnontramos el abuelo del nodo
        if abuelo is None: #Si no tiene abuelo tampoco tiene tío
            return None
        if data > abuelo.data: #Usando al abuelo, nos vamos al subárbol en el que no se encuentre el nodo que buscamos
            return abuelo.left
        return abuelo.right
    
    def LevelTraversal(self):
        """Recorrido por nivel recursivo"""
        self.CalculateLevel() #Recalculamos el nivel como validación de que sea correcto
        h = self.AlturaNodo(self.root) #Calculamos la altura del árbol
        for i in range(1, h + 2): #Hacemos recorridos del árbol h veces
            self.CurrentLevel(self.root, i)

    def CurrentLevel(self, root: Node, level):
        """Imprime los nodos dependiendo del nivel"""
        if root is None:
            return
        if level == 1: #Cuando el nivel con el que se llama la función sea 1, se imprime el nodo
            print(root.data, end=" ")
        elif level > 1:
            self.CurrentLevel(root.left , level-1) #Nos movemos en el árbol y vamos disminuyendo el nivel
            self.CurrentLevel(root.right , level-1) #a la vez, para que cuando sea 1 se imprima

def main():
    pass

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
'''
nodo = tk.Label(ventana, text=tree.insert(10),
                                 font=Fuente_principal, disabledforeground=None, bg="#FFFFFF")
# Ubicación (x,y) del label
nodo.place(x=470, y=50) 
'''


abuelo = tree.EncontrarAbuelo(tree.root, 10)
tio = tree.EncontrarTio(50)
#print(f"{abuelo} y {tio}")
nodo = tree.BuscarNodo(tree.root, 40)
#print(nodo)

tree2 = Tree()
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for num in nums:
    tree2.insert(num)
print()
tree2.preorder(tree2.root)
tree2.delete(10)
print()
tree2.preorder(tree2.root)
tio = tree.EncontrarTio(10)
print(f"{abuelo} y {abuelo.right}")
nodo = tree.BuscarNodo(tree.root, 60)
print(nodo)


# El mainloop lleva el registro de todo lo que está sucediendo en la ventana:
ventana.mainloop()

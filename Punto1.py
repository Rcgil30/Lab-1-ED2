class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Node = None
        self.right: Node = None
        self.height = 1

class Tree:
    def __init__(self) -> None:
        self.root: Node = None
    
    def obtenerAltura(self, root: Node):
        if root is None:
            return 0
        return root.height

    def Balance(self, root: Node):
        if root is None:
            return 0
        return self.obtenerAltura(root.left) - self.obtenerAltura(root.right)
    
    def RotacionIzquierda(self, root: Node):
        child = root.left
        root.left = child.right
        child.right = root
        root.height = 1 + max(self.obtenerAltura(root.left),
                         self.obtenerAltura(root.right))
        child.height = 1 + max(self.obtenerAltura(child.left),
                         self.obtenerAltura(child.right))
        return child

    def RotacionDerecha(self, root: Node):
        child = root.right
        root.right = child.left
        child.left = root
        root.height = 1 + max(self.obtenerAltura(root.left),
                         self.obtenerAltura(root.right))
        child.height = 1 + max(self.obtenerAltura(child.left),
                         self.obtenerAltura(child.right))
        return child

    def insertarNodo(self, root: Node, data):
        if root is None:
            return Node(data=data)
        elif data < root.data:
            root.left = self.insertarNodo(root.left, data)
        else:
            root.right = self.insertarNodo(root.right, data)
        root.height = 1 + max(self.obtenerAltura(root.left),
                           self.obtenerAltura(root.right))
        balance = self.Balance(root)
        #Rotación simple izquierda
        if balance > 1 and data < root.right.data:
            return self.RotacionIzquierda(root)
        #Rotación simple derecha
        if balance > -1 and data < root.left.data:
            return self.RotacionDerecha(root)    
        #Rotación doble izquierda
        if balance > 1 and data > root.right.data:
            root.left = self.RotacionDerecha(root.left)
            return self.RotacionIzquierda(root)
        #Rotación doble derecha
        if balance > -1 and data < root.left.data:
            root.right = self.RotacionDerecha(root.right)
            return self.RotacionDerecha(root)    

        return root
    
    def preOrder(self, root:Node):
 
        if not root:
            return
 
        print("{0} ".format(root.data), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

tree = Tree()
tree.root = tree.insertarNodo(tree.root, 10)
tree.root = tree.insertarNodo(tree.root, 20)
tree.root = tree.insertarNodo(tree.root, 30)
tree.root = tree.insertarNodo(tree.root, 40)
tree.root = tree.insertarNodo(tree.root, 50)
tree.root = tree.insertarNodo(tree.root, 25)



tree.preOrder(tree.root)
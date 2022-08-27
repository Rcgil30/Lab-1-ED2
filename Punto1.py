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
            return Node(data)
        elif data < root.data:
            root.left = self.insertarNodo(root.left, data)
        else:
            root.right = self.insertarNodo(root.right, data)
        root.height = 1 + max(self.obtenerAltura(root.left),
                           self.obtenerAltura(root.right))
        balance = self.Balance(root)
        #Rotación simple izquierda
        if (balance > 1 and data < root.left.data):
            return self.RotacionIzquierda(root)
        #Rotación simple derecha
        if (balance < -1 and data > root.right.data):
            return self.RotacionDerecha(root)    
        #Rotación doble izquierda
        if (balance > 1 and data > root.left.data):
            root.left = self.RotacionDerecha(root.left)
            return self.RotacionIzquierda(root)
        #Rotación doble derecha
        if (balance < -1 and data < root.right.data):
            root.right = self.RotacionIzquierda(root.right)
            return self.RotacionDerecha(root)    
        return root
    
    def getMinValueNode(self, root: Node):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)

    def delete(self, root: Node, data):
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
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
            root.right = self.delete(root.right,
                                      temp.data)
 
        # If the tree has only one node,
        # simply return it
        if root is None:
            return root
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.obtenerAltura(root.left),
                            self.obtenerAltura(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.Balance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.Balance(root.left) >= 0:
            return self.RotacionIzquierda(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.Balance(root.right) <= 0:
            return self.RotacionDerecha(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.Balance(root.left) < 0:
            root.left = self.RotacionDerecha(root.left)
            return self.RotacionIzquierda(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.Balance(root.right) > 0:
            root.right = self.RotacionIzquierda(root.right)
            return self.RotacionDerecha(root)
 
        return root

    

    def LevelOrder(self, root):
        h = self.height(root)
        for i in range(1, h+1):
            self.CurrentLevel(root, i)
    def CurrentLevel(self, root: Node, level):
        if root is None:
            return
        if level == 1:
            print(root.data,end=" ")
        elif level > 1 :
            self.CurrentLevel(root.left , level-1)
            self.CurrentLevel(root.right , level-1)
    def height(self, node: Node):
        if node is None:
            return 0
        else :
            lheight = self.height(node.left)
            rheight = self.height(node.right)
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1

tree = Tree()
tree.root = tree.insertarNodo(tree.root, 10)
tree.root = tree.insertarNodo(tree.root, 20)
tree.root = tree.insertarNodo(tree.root, 30)
tree.root = tree.insertarNodo(tree.root, 40)
tree.root = tree.insertarNodo(tree.root, 50)
tree.root = tree.insertarNodo(tree.root, 25)


tree.LevelOrder(tree.root)
print()
tree2 = Tree()
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for num in nums:
    tree2.root = tree2.insertarNodo(tree2.root, num)
tree2.preOrder(tree2.root)
print()
tree2.root = tree2.delete(tree2.root, 10)
tree2.preOrder(tree2.root)





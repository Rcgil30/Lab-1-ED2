class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Node = None
        self.right: Node = None
        self.level = 0

    def __repr__(self) -> str:
        return f"data: {self.data}"

class Tree():
    def __init__(self) -> None:
        self.root: Node = None
    
    def BuscarNodo(self, root: Node, data):
        if root is None:
            return None
        if root.data == data:
            return root
        if data > root.data:
            return self.BuscarNodo(root.right, data)
        else: 
            return self.BuscarNodo(root.left, data)

    def _insert_(self, root: Node, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self._insert_(root.left, data)
        else:
            root.right = self._insert_(root.right, data)

        self.CalculateLevel()

        balance = self.Balance(root)
        if ((balance < -1) and data <= root.left.data):
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
        if self.BuscarNodo(data) is None:
            print("Nodo no encontrado")
        else:
            self._delete_()

    def _delete_(self, root: Node, data):
        if data < root.data:
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


    def CalculateLevel(self):
        node = self.root
        s = [node]
        while len(s) > 0:
            node = s.pop(0)
            if node.left is not None:
                s.append(node.left)
                node.left.level = node.level + 1
            if node.right is not None:
                s.append(node.right)
                node.right.level = node.level + 1

    def BuscarMax(self, root: Node):
        if root is None:
            return 0
        node = root
        s = [node]
        while len(s) > 0:
            node = s.pop(0)
            if node.left is not None:
                s.append(node.left)
            if node.right is not None:
                s.append(node.right)
        return node.level

    def Balance(self, root: Node):
        rheight = self.BuscarMax(root.right) 
        lheight = self.BuscarMax(root.left) 
        if (rheight != 0):
            rheight -= root.level
        if (lheight != 0):
            lheight -= root.level
        return rheight - lheight

    def insert(self, data): 
        if self.root is None:
            self.root = Node(data)
        else:
            self.root = self._insert_(self.root, data)
    
    def RotacionIzquierda(self, root: Node):
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
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def AlturaNodo(self, root:Node):
        temp = self.BuscarMax(root)
        return temp - root.level

    def EncontrarAbuelo(self, root:Node, data):
        if root is None:
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


tree = Tree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)
tree.preorder(tree.root)

abuelo = tree.EncontrarAbuelo(tree.root, 10)
tio = tree.EncontrarTio(10)
print(f"{abuelo} y {abuelo.right}")
nodo = tree.BuscarNodo(tree.root, 60)
print(nodo)

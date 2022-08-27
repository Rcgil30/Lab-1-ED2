class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Node = None
        self.right: Node = None
        self.level = 0

class Tree():
    def __init__(self) -> None:
        self.root: Node = None
    
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

tree = Tree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)
tree.preorder(tree.root)


"""
tree.preorder(tree.root.left.left.data)
tree.insert(2)
tree.preorder(tree.root)
"""
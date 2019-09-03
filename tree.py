class Node():

    def __init__(self, value, left, right):
        self.left = left
        self.right = right
        self.value = value

    def printInOrder(self):
        if (self.left is not None):
            self.left.printInOrder()
        print(self.value)
        if (self.right is not None):
            self.right.printInOrder()

    def contains(self, value):
        if (self.value == value):
            return True
        elif (value < self.value):
            if (self.left is not None):
                return self.left.contains(value)
        else:
            if (self.right is not None):
                return self.right.contains(value)

        return False


class Tree():

    def __init__(self, value):
        self.head = Node(value, None, None)

    def add(self, value):
        current = self.head
        isEnd = False
        while (not isEnd):
            if (value <= current.value):
                if (current.left is None):
                    current.left = Node(value, None, None)
                    isEnd = True
                else:
                    current = current.left
            else:
                if (current.right is None):
                    current.right = Node(value, None, None)
                    isEnd = True
                else:
                    current = current.right

    def printInOrder(self):
        self.head.printInOrder()

    def contains(self, value):
        return self.head.contains(value)


tree = Tree(5)
tree.add(4)
tree.add(5)
print(tree.contains(7))
tree.add(7)
print(tree.contains(7))
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(6)
print(tree.contains(11))
tree.add(11)

tree.printInOrder()

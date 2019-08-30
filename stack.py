import node


class Stack():

    head = None

    def push(self, value):
        if (self.head == None):
            self.head = node.Node(value, None)
        else:
            buf = self.head
            self.head = node.Node(value, None)
            self.head.next = buf

    def pop(self):
        if (self.head != None):
            res = self.head
            self.head = self.head.next
            return res.data
        return None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

pass

import node


class Queue():

    head = None

    def enqueue(self, value):
        if (self.head == None):
            self.head = node.Node(value, None)
        else:
            current = self.head
            isEnd = False
            while (not isEnd):
                if (current.next == None):
                    current.next = node.Node(value, None)
                    isEnd = True
                current = current.next

    def dequeue(self):
        if (self.head != None):
            res = self.head
            self.head = self.head.next
            return res.data
        return None


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

pass

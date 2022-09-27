class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Pilha:
    def __init__(self):
        self.top = Node(None)
        self.size = 0
    
    def __str__(self):
        cur = self.top.next
        out = ""

        while cur:
            out += str(cur.value) + "\n"
            cur = cur.next

        return out

    def isempty(self):
        return self.size == 0

    def push(self,value):
        node = Node(value)
        node.next = self.top.next
        self.top.next = node
        self.size += 1

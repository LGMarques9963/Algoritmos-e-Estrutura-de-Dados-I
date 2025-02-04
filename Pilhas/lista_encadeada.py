class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Lista:
    def __init__(self):
        self.first = Node(None) 


    def __str__(self):
        cur = self.first.next
        out = ""

        while cur:
            out += str(cur.value) + "\n"
            cur = cur.next

        return out

    #TODO implement this
    def insert(self,value):
        first = _insert(value, first)
    
    def _insert(self,value,node):
        if (node == None):
            return Node(value)
        node.next = _insert(value,node.next)
        return node
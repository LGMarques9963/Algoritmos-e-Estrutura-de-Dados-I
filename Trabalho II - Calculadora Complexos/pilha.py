class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Pilha:
    def __init__(self):
        self.top = Node("Head")
        self.size = 0

    def __str__(self):
        cur = self.top.next
        out = ""
        while cur:
            if cur.value[1] >=0:
                out += str(cur.value[0]) + " + " + str(cur.value[1]) + "i\n"
            else:
                out += str(cur.value[0]) + " - " + str(cur.value[1] * (-1)) + "i\n"
            cur = cur.next
        return out

    def isempty(self):
        return self.size == 0

    def push(self,value):
        node = Node(value)
        node.next = self.top.next
        self.top.next = node
        self.size+=1

    def pop(self):
        if not self.isempty():
            remove = self.top.next
            self.top.next = self.top.next.next
            self.size -= 1
            return remove.value
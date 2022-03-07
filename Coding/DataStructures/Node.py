

class SListNode:
   def __init__(self, data, nextNode=None):
       self.data = data
       self.next = nextNode


class DListNode:
    def __init__(self, data, prevNode=None, nextNode=None):
        self.data = data
        self.prev = prevNode
        self.next = nextNode


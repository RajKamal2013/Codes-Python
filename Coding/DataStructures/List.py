from Coding.DataStructures.Node import SListNode

class SLinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert(self, data):
        newNode = SListNode(data)
        newNode.next = self.head
        self.head = newNode
        return self.head

    def append(self, data):
        newNode = SListNode(data)
        newNode.next = None;

        if self.get_head() is None:
            self.head = newNode
            return self.head

        tail = self.get_head()
        while tail.next is not None:
            tail = tail.next
        tail.next = newNode
        return self.head

    def get_List(self):
        arr = []
        if self.get_head() is None:
            return arr

        temp = self.get_head()
        while temp is not None:
            arr.append(temp.data)
            temp = temp.next
        return arr

    def contains(self, data):
        temp = self.get_head();
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next

        return False

    def remove(self, data):
        if self.get_head() is None:
            return
        listItr = self.get_head()
        prev = None
        while listItr is not None:
            if listItr.data == data:
                break
            else:
                prev = listItr
                listItr = listItr.next

        if listItr is None:
            return
        else:
            if prev is None:
                temp = listItr
                self.head = listItr.next

            else:
                temp = listItr
                prev.next = listItr.next

            temp = None

    def remove_last(self):
        listItr = self.get_head()
        if listItr is None:
            return
        else:
            prev = None
            while listItr.next is None:
                prev = listItr
                listItr = listItr.next

            temp = listItr
            if prev is not None:
                prev.next = listItr.next
            else:
                temp = listItr
                self.head = None
            temp = None

    def remove_first(self):
        if self.head is None:
            return

        temp = self.head
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next

        temp = None

    def size(self):
        count = 0
        listItr = self.get_head()
        while listItr is not None:
            count = count + 1
            listItr = listItr.next
        return count



















from adt_doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def isEmpty(self):
        return self.storage.get_length() == 0

    def enqueue(self, item):
        self.storage.push_back(item)

    def dequeue(self):
        node = self.storage.front()
        if node is not None:
            return node.remove()
        else:
            return False

    def getFront(self):
        return self.storage.front()

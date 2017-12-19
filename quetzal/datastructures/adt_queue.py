from . import AdtDoublyLinkedList

class AdtQueue:
    def __init__(self):
        self.storage = AdtDoublyLinkedList()

    def isEmpty(self):
        return self.storage.getLength() == 0

    def enqueue(self, item):
        self.storage.insertEnd(item)

    def dequeue(self):
        node = self.storage.searchNode(1)
        if node is not None:
            return self.storage.retrieve(1)[0]
        else:
            return False

    def getFront(self):
        return self.storage.searchNode(0)

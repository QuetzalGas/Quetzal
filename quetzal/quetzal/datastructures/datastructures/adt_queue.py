from . import AdtDoublyLinkedList


class AdtQueue:
    def __init__(self):
        self.storage = AdtDoublyLinkedList()

    def is_empty(self):
        return len(self.storage) == 0

    def enqueue(self, item):
        self.storage[len(self.storage)] = item

    def dequeue(self):
        node = self.storage[0]
        if node is not None:
            del self.storage[0]
            return node
        else:
            return False

    def get_front(self):
        return self.storage[0]

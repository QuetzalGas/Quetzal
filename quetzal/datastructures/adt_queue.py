from . import AdtDoublyLinkedList


class AdtQueue:
    def __init__(self):
        self.storage = AdtDoublyLinkedList()

    def is_empty(self):
        return self.storage.get_length() == 0

    def enqueue(self, item):
        self.storage.insert_end(item)

    def dequeue(self):
        node = self.storage.search_node(1)

        if node is not None:
            return self.storage.retrieve(1)[0]
        else:
            return False

    def get_front(self):
        return self.storage.search_node(0)

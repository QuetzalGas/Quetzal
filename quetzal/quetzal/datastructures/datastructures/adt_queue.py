from . import AdtDoublyLinkedList


class AdtQueue:
    def __init__(self):
        """
        Initialises a new queue.
        """
        self.storage = AdtDoublyLinkedList()

    def is_empty(self):
        """ Checks if the queue is empty.

        :return: True if the storage is empty, false otherwise.
        """
        return len(self.storage) == 0

    def enqueue(self, item):
        """ Enqueues an item.

        :param item: The item to be added to the queue.
        """
        self.storage[len(self.storage)] = item

    def dequeue(self):
        """ Dequeues an item from the queue.

        :return: The item or false if the queue is empty.
        """
        node = self.storage[0]
        if node is not None:
            del self.storage[0]
            return node
        else:
            return False

    def get_front(self):
        """ Returns the front of the queue without dequeueing it.

        :return: The front of the queue.
        """
        return self.storage[0]

    def __repr__(self):
        """ String with dot representation of the queue.

        :return: String with all the info of the queue.
        """
        output = 'digraph queue {\n node [shape=record];\n'
        output += '  node1 [label="'

        for i in range(len(self.storage)):
            value = self.storage[i]
            output += str(value)
            if i != len(self.storage) - 1:
                output += '|'
        output += '"];\n  node1;\n'

        output += '}'
        return output

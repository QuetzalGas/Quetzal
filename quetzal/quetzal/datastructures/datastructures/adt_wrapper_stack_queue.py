from .adt_queue import *
from .adt_stack import *

STACK = 0
QUEUE = 1


class StackQueue:
    def __init__(self, struct):
        """ Initialises a new wrapper with either stack or queue.

        :param struct: The type of structure the wrapper needs to address.
        """
        if not 0 <= struct <= 1:
            raise TypeError("Invalid type for wrapper!")
        self.struct = struct
        if struct == STACK:
            self.table = AdtStack()
        else:
            self.table = AdtQueue()

    def is_empty(self):
        """ Checks whether the structure is empty.

        :return: True if the structure is empty, false otherwise.
        """
        return self.table.is_empty()

    def insert(self, item):
        """ Inserts a new element.

        :param item: The item to be inserted.
        """
        if self.struct == STACK:
            self.table.push(item)
        else:
            self.table.enqueue(item)

    def delete(self):
        """ Deletes an item from the structure.

        :return: Returns the deleted item.
        """
        if self.struct == STACK:
            return self.table.pop_and_return()
        else:
            return self.table.dequeue()

    def peek(self):
        """ Looks at the item at the top of the stack or front of the queue.

        :return: The item at the top or front.
        """
        if self.struct == STACK:
            return self.table.peek()
        else:
            return self.table.get_front()
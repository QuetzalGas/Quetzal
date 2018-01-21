class _Node:
    def __init__(self, item, next=None):
        """ Creates a new node.
        :param item: Element that contains data.
        :param next: Next element.
        """
        self.item = item
        self.next = next


class AdtCircularLinkedList:
    def __init__(self):
        """
        Creates a new circular linked list with a dummy head node.
        """
        self.dummy_head = _Node(None, None)
        self.dummy_head.next = self.dummy_head
        self.head = self.dummy_head

    def __del__(self):
        """
        Deletes the list.
        """
        self.dummy_head.next = self.dummy_head
        self.head = self.dummy_head

    def is_empty(self):
        """ Checks if the list is empty.

        :return: True if the list is empty. False otherwise.
        """
        return self.dummy_head.next == self.dummy_head

    def get_length(self):
        """ Returns the amount of elements in the list.

        :return: The number of elements in the list.
        """
        length = 0
        if not self.is_empty():
            cur = self.head
            while cur.next is not self.dummy_head:
                cur = cur.next
                length += 1
        return length

    def __setitem__(self, index, new_item):
        """ Adds a new element at a given location.

        :param index: Position where the new element needs to be added.
        :param new_item: Element that needs to be added.
        :raises: TypeError if new_item isn't the same type as the rest. KeyError if the given index is incorrect.
        """

        if not self.is_empty():
            if not isinstance(new_item, type(self.head.next.item)):
                raise TypeError("Item is not of same type as the rest!")
        if (index >= 0) and (index <= (self.get_length())):
            cur = self.head
            for i in range(index):
                cur = cur.next
            cur.next = _Node(new_item, cur.next)
        else:
            raise KeyError("Index is out of range!")

    def __delitem__(self, index):
        """ Delete the element on position 'index'.

        :param index: Position of the element that needs to be deleted.
        :raise: KeyError if there is nothing on the given index.
        """
        if 0 <= index < self.get_length():
            cur = self.head
            prev = _Node(None, cur)
            # +1 because we take the dummy node as cur the first time
            for i in range(index+1):
                cur = cur.next
                prev = prev.next
            prev.next = cur.next
        else:
            raise KeyError("Index out of range!")

    def __getitem__(self, index):
        """ Returns the element on position 'index'.

        :param index: Position of the element.
        :raise: KeyError if there is nothing on the given index.
        :return The item on the given index.
        """
        if 0 <= index < self.get_length():
            cur = self.head
            for i in range(index + 1):
                cur = cur.next
            return cur.item
        else:
            raise KeyError("Index out of range!")

    def __contains__(self, item):
        """ Searches for an item in the list.

        :param item: The item to search.
        :return: True if the item is in the list, false otherwise.
        """
        cur = self.head
        for i in range(self.get_length() + 1):
            cur = cur.next
            if cur.item == item:
                return True
        return False

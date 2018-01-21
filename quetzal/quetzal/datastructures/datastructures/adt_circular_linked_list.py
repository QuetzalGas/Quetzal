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

    def __len__(self):
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
        :raise TypeError if new_item is not the same type as the items in the list
        :raise IndexError if index is out of range
        """

        if not self.is_empty():
            if not isinstance(new_item, type(self.head.next.item)):
                raise TypeError("")

        if (index >= 0) and (index <= (len(self))):
            cur = self.head
            for i in range(index):
                cur = cur.next
            cur.next = _Node(new_item, cur.next)
        else:
            raise IndexError("")

    def __delitem__(self, index):
        """ Delete the element on position 'index'.

        :param index: positie van het element dat verwijderd moet worden.
        :raise IndexError if index is out of range
        """
        if 0 <= index < len(self):
            cur = self.head
            prev = _Node(None, cur)
            for i in range(index+1):
                cur = cur.next
                prev = prev.next
            prev.next = cur.next
        else:
            raise IndexError("")

    def __getitem__(self, index):
        """ Returns the element on position 'index".

        :param index: positie van het element.
        :raise IndexError if index is out of range
        :return: element
        """
        if 0 <= index < len(self):
            cur = self.head
            for i in range(index+1):
                cur = cur.next
            return cur.item
        else:
            raise IndexError("")

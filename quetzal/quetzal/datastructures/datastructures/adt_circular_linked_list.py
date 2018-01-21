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

    def insert(self, index, new_item):
        """ Adds a new element at a given location.

        :param index: Position where the new element needs to be added.
        :param new_item: Element that needs to be added.
        :return: True als het toevoegen gelukt is. #TODO weg en vervangen met raise
        >>> l = AdtCircularLinkedList()
        >>> l.insert(0,10)
        False
        >>> l.insert(1,0)
        True
        >>> l.insert(2,5)
        True
        >>> l.insert(3,"abc")
        False
        >>> l.insert(3,7)
        True
        >>> l.insert(10, 8)
        False
        >>> l.insert(4, -56)
        True
        >>> l.get_length()
        4
        """

        if not self.is_empty():
            if not isinstance(new_item, type(self.head.next.item)):
                return False

        if (index >= 0) and (index <= (self.get_length())):
            cur = self.head
            for i in range(index - 1): #TODO -1 weg?
                cur = cur.next
            cur.next = _Node(new_item, cur.next)
            return True
        return False

    def delete(self, index):
        """ Delete the element on position 'index'.

        :param index: positie van het element dat verwijderd moet worden.
        :return: True als het verwijderen gelukt is.
        >>> l = AdtCircularLinkedList()
        >>> l.insert(1,0)
        True
        >>> l.insert(2,5)
        True
        >>> l.insert(3,7)
        True
        >>> l.insert(4, -56)
        True
        >>> l.delete(2)
        True
        >>> l.delete(2)
        True
        >>> l.get_length()
        2
        >>> l.retrieve(2)
        (-56, True)
        >>> l.delete(0)
        False
        >>> l.delete(10)
        False
        """
        if 0 <= index < self.get_length():
            cur = self.head
            prev = _Node(None, cur)
            for i in range(index):
                cur = cur.next
                prev = prev.next
            prev.next = cur.next
            return True
        return False

    def retrieve(self, index):
        """ Returns the element on position 'index".

        :param index: positie van het element.
        :return: element, True als het opvragen gelukt is.
        >>> l = AdtCircularLinkedList()
        >>> l.insert(1,0)
        True
        >>> l.insert(2,5)
        True
        >>> l.insert(3,7)
        True
        >>> l.insert(4, -56)
        True
        >>> l.retrieve(0)
        (None, False)
        >>> l.retrieve(2)
        (5, True)
        >>> l.retrieve(5)
        (None, False)
        >>> l.retrieve(4)
        (-56, True)
        >>> l.delete(1)
        True
        >>> l.retrieve(1)
        (5, True)
        """
        if 0 <= index < self.get_length():
            cur = self.head
            for i in range(index):
                cur = cur.next
            return cur.item, True
        return None, False

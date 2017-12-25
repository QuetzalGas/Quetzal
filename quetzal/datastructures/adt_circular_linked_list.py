class _Node:
    def __init__(self, item, next=None):
        """
        Creëert een nieuw element node.
        :param item: Element dat de node bevat.
        :param next: Volgende element.
        """
        self.item = item
        self.next = next


class AdtCircularLinkedList:
    def __init__(self):
        """
        Creëert een lege circulair gelinkte ketting met een dummy head node.
        >>> l = AdtCircularLinkedList()
        >>> l.head == l.dummy_head
        True
        >>> l.dummy_head.next == l.dummy_head
        True
        """
        self.dummy_head = _Node(None, None)
        self.dummy_head.next = self.dummy_head
        self.head = self.dummy_head

    def destroy_list(self):
        """
        Wist een ketting.
        >>> l = AdtCircularLinkedList()
        >>> l.insert(1,"abc")
        True
        >>> l.destroy_list()
        >>> l.head == l.dummy_head
        True
        >>> l.dummy_head.next == l.dummy_head
        True
        """
        self.dummy_head.next = self.dummy_head
        self.head = self.dummy_head

    def is_empty(self):
        """
        Bepaalt of een gelinkte ketting leeg is.
        :return: True als de ketting leeg is.
        >>> l = AdtCircularLinkedList()
        >>> l.is_empty()
        True
        >>> l.insert(1,"abc")
        True
        >>> l.is_empty()
        False
        >>> l.insert(2,"def")
        True
        >>> l.insert(3,"ghi")
        True
        >>> l.is_empty()
        False
        >>> l.destroy_list()
        >>> l.is_empty()
        True
        """
        return self.dummy_head.next == self.dummy_head

    def get_length(self):
        """
        Geeft het aantal elementen in de gelinkte ketting.
        :return: aantal elementen.
        >>> l = AdtCircularLinkedList()
        >>> l.get_length()
        0
        >>> l.insert(1,"abc")
        True
        >>> l.get_length()
        1
        >>> l.insert(2,"def")
        True
        >>> l.insert(3,"ghi")
        True
        >>> l.get_length()
        3
        >>> l.destroy_list()
        >>> l.get_length()
        0
        """
        length = 0
        if not self.is_empty():
            cur = self.head
            while cur.next is not self.dummy_head:
                cur = cur.next
                length += 1
        return length

    def insert(self, index, new_item):
        """
        Voegt het element 'newItem' toe op positie 'index' in de gelinkte ketting, als
        1 <= index <= get_length()+1.
        :param index: positie waar het element moet toegevoegd worden.
        :param newItem: element dat toegevoegd moet worden.
        :return: True als het toevoegen gelukt is.
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

        if (index >= 1) and (index <= (self.get_length() + 1)):
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            cur.next = _Node(new_item, cur.next)
            return True
        return False

    def delete(self, index):
        """
        Verwijdert het element op positie 'index' in de gelinkte ketting, als
        1 <= index <= get_length().
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
        if index >= 1 and index <= self.get_length():
            cur = self.head
            prev = _Node(None, cur)
            prev = _Node(None, cur)
            for i in range(index):
                cur = cur.next
                prev = prev.next
            prev.next = cur.next
            return True
        return False

    def retrieve(self, index):
        """
        Geeft het element op positie 'index' van de gelinkte ketting terug, als
        1 <= index <= get_length().
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
        if (index >= 1) and (index <= self.get_length()):
            cur = self.head
            for i in range(index):
                cur = cur.next
            return cur.item, True
        return None, False

from Node import Node
class CircularLinkedList:
    def __init__(self):
        """
        Creëert een lege circulair gelinkte ketting met een dummy head node.
        >>> l = CircularLinkedList()
        >>> l.head == l.dummyhead
        True
        >>> l.dummyhead.next == l.dummyhead
        True
        """
        self.dummyhead = Node(None, None)
        self.dummyhead.next = self.dummyhead
        self.head = self.dummyhead

    def destroyList(self):
        """
        Wist een ketting.
        >>> l = CircularLinkedList()
        >>> l.insert(1,"abc")
        True
        >>> l.destroyList()
        >>> l.head == l.dummyhead
        True
        >>> l.dummyhead.next == l.dummyhead
        True
        """
        self.dummyhead.next = self.dummyhead
        self.head = self.dummyhead

    def isEmpty(self):
        """
        Bepaalt of een gelinkte ketting leeg is.
        :return: True als de ketting leeg is.
        >>> l = CircularLinkedList()
        >>> l.isEmpty()
        True
        >>> l.insert(1,"abc")
        True
        >>> l.isEmpty()
        False
        >>> l.insert(2,"def")
        True
        >>> l.insert(3,"ghi")
        True
        >>> l.isEmpty()
        False
        >>> l.destroyList()
        >>> l.isEmpty()
        True
        """
        return self.dummyhead.next == self.dummyhead

    def getLength(self):
        """
        Geeft het aantal elementen in de gelinkte ketting.
        :return: aantal elementen.
        >>> l = CircularLinkedList()
        >>> l.getLength()
        0
        >>> l.insert(1,"abc")
        True
        >>> l.getLength()
        1
        >>> l.insert(2,"def")
        True
        >>> l.insert(3,"ghi")
        True
        >>> l.getLength()
        3
        >>> l.destroyList()
        >>> l.getLength()
        0
        """
        length = 0
        if not self.isEmpty():
            cur = self.head
            while cur.next is not self.dummyhead:
                cur = cur.next
                length += 1
        return length

    def insert(self, index, newItem):
        """
        Voegt het element 'newItem' toe op positie 'index' in de gelinkte ketting, als
        1 <= index <= getLength()+1.
        :param index: positie waar het element moet toegevoegd worden.
        :param newItem: element dat toegevoegd moet worden.
        :return: True als het toevoegen gelukt is.
        >>> l = CircularLinkedList()
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
        >>> l.getLength()
        4
        """

        if not self.isEmpty():
            if not isinstance(newItem,type(self.head.next.item)):
                return False

        if index >= 1 and index <= self.getLength()+1:
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            newNode = Node(newItem, cur.next)
            cur.next = newNode
            return True
        return False

    def delete(self, index):
        """
        Verwijdert het element op positie 'index' in de gelinkte ketting, als
        1 <= index <= getLength().
        :param index: positie van het element dat verwijderd moet worden.
        :return: True als het verwijderen gelukt is.
        >>> l = CircularLinkedList()
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
        >>> l.getLength()
        2
        >>> l.retrieve(2)
        (-56, True)
        >>> l.delete(0)
        False
        >>> l.delete(10)
        False
        """
        if index >= 1 and index <= self.getLength():
            cur = self.head
            prev = Node(None, cur)
            prev = Node(None, cur)
            for i in range(index):
                cur = cur.next
                prev = prev.next
            prev.next = cur.next
            return True
        return False

    def retrieve(self, index):
        """
        Geeft het element op positie 'index' van de gelinkte ketting terug, als
        1 <= index <= getLength().
        :param index: positie van het element.
        :return: element, True als het opvragen gelukt is.
        >>> l = CircularLinkedList()
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
        if index >= 1 and index <= self.getLength():
            cur = self.head
            for i in range(index):
                cur = cur.next
            return cur.item, True
        return None, False


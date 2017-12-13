from Node import Node
class Stack:

    def __init__(self):
        """
        Creëert een lege stack.
        >>> s = Stack()
        >>> s.createStack()
        >>> s.top is None
        True
        """
        self.top = None

    def destroyStack(self):
        """
        Wist een stack.
        >>> s = Stack()
        >>> s.createStack()
        >>> s.destroyStack()
        >>> s.top is None
        True
        >>> s.push(6)
        True
        >>> s.top is None
        False
        >>> s.destroyStack()
        >>> s.top is None
        True
        """
        self.top = None

    def isEmpty(self):
        """
        Bepaalt of een stack leeg is.
        :return: boolean True als de stack leeg is.
        >>> s = Stack()
        >>> s.createStack()
        >>> s.isEmpty()
        True
        >>> s.push(6)
        True
        >>> s.isEmpty()
        False
        """
        return self.top is None

    def push(self, newItem):
        """
        Voegt het element 'newItem' toe op de top van de stack,
        indien het element van hetzelfde type is als de andere elementen van de stack.
        'success' duidt aan of het toevoegen gelukt is.
        :param newItem: nieuw element op de top van de stack.
        :return: boolean True als het gelukt is.
        >>> s = Stack()
        >>> s.createStack()
        >>> s.push("a")
        True
        >>> s.push(6)
        False
        >>> s.push("abc")
        True

        """
        if not self.isEmpty():
            if not isinstance(newItem,type(self.top.item)):
                return False
        self.top = Node(newItem, self.top)
        return True

    # def pop(self):
    #     """
    #     Verwijdert de top van de stack.
    #     :return: True als het gelukt is.
    #     >>> s = Stack()
    #     >>> s.createStack()
    #     >>> s.pop()
    #     False
    #     >>> s.push(6)
    #     True
    #     >>> s.push(8)
    #     True
    #     >>> s.push(10)
    #     True
    #     >>> s.pop()
    #     True
    #     """
    #     if self.isEmpty():
    #         return False
    #     stackTop = self.top
    #     self.top = self.top.next
    #     return True

    def pop(self):
        """
        Verwijdert de top van de stack maar plaatst het eerst in 'stackTop'.
        :return: stackTop en boolean True als het gelukt is.
        >>> s = Stack()
        >>> s.createStack()
        >>> s.pop()
        (None, False)
        >>> s.push(6)
        True
        >>> s.push(8)
        True
        >>> s.push(10)
        True
        >>> s.pop()
        (10, True)
        >>> s.pop()
        (8, True)
        """
        if self.isEmpty():
            return None, False
        stackTop = self.top.item
        self.top = self.top.next
        return (stackTop, True)

    def getTop(self):
        """
        Geeft de top van de stack terug, zonder de stack te wijzigen.
        :return: top van de stack, True als het gelukt is.
        >>> s = Stack()
        >>> s.createStack()
        >>> s.getTop()
        (None, False)
        >>> s.push(6)
        True
        >>> s.getTop()
        (6, True)
        >>> s.push(8)
        True
        >>> s.push(10)
        True
        >>> s.getTop()
        (10, True)
        """
        if self.isEmpty():
            return None, False
        return self.top.item, True


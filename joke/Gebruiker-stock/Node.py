class Node:
    def __init__(self, item, next = None):
        """
        Creëert een nieuw element node.
        :param item: Element dat de node bevat.
        :param next: Volgende element.
        """
        self.item = item
        self.next = next

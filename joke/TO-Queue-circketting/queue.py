from ketting import circulaire_ketting,Node

class queue:
    def __init__(self):
        self.list = circulaire_ketting()

    def createQueue(self):
        self.list = circulaire_ketting()

    def destroyQueue(self):
        """
        Verwijdert de queue.
        """
        del self.list

    def QueueIsEmpty(self):
        """
        Checkt of de queue leeg is.
        :return: geeft  False indien leeg
                        True indien niet leeg
        """
        return self.list.isEmpty()

    def enqueue(self, queueItem):
        """
        Voegt een nieuw item achteraan de queue toe. Omdat de queue geïmplementeerd is dmv een circulaire ketting met de head verwijzend
            naar het laatst toegevoegde element, wordt het item op index 1 in de lijst toegevoegd.
        :param item: het item dat wordt toegevoegd
        :return: geeft  True indien het toevoegen gelukt is
                        False indien het niet gelukt is
        """
        mkNode = Node(queueItem)     #maakt een Node dat 'queueItem' bevat als item
        if self.list.insert(1, mkNode) is True:
            return True
        else:
            return False

    def dequeue(self):
        """
        Verwijdert de de front van de queue.
        geval 1: er zijn meer dan 1 items in de queue, dan moet item op index 2 verwijderd worden (eerst toegevoegde item in de circulaire ketting met headpointer naar laatste item)
        geval 2: er is 1 item in de queue, dan moet het item op index 1 verwijderd worden uit de lijst.
        :return: geeft een  (True, queueFront) als de lijst(queue) niet leeg is.
                            (False, None) als de lijst(queue) leeg is. Het kan in dit geval geen front teruggeven.
        """
        if self.list.isEmpty() is False:
            if self.list.getLength() > 1:
                (bool, queueFront) = self.list.retrieve(2)
                self.list.delete(2)
            else:
                (bool, queueFront) = self.list.retrieve(1)
                self.list.delete(1)
            return (True, queueFront)

        else:
            return (False, None)

    def getFront(self):
        """
        Als de queue niet leeg is, geeft het de front van de queue (eerst toegevoegde item in lijst) terug.
        :return: geeft      (False, None) als de lijst (queue) leeg is, er is geen front om terug te geven
                            (True, queueFront) als de lijst niet leeg is:   - geval 1: bevat maar 1 item, geeft item op index 1 in lijst terug
                                                                            - geval 2: bevat meer dan 1 item, geeft item op index 2 in lijst terug

        """
        if self.list.isEmpty() is True:
            return (False, None)
        else:
            if self.list.getLength() > 1:
                (bool, queueFront) = self.list.retrieve(2)
            else:
                (bool, queueFront) = self.list.retrieve(1)
            return (True, queueFront)

    def print(self):
        """
        Hulpmiddel om de queue te testen. Print de items.
        """
        self.list.print()


class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
class Head:
    def __init__(self, next = None):
        self.next = next

class circulaire_ketting:
    def __init__(self, count = 0):
        """
        Maakt een circulaire ketting aan. Deze ketting heeft een head(pointer) die altijd naar het laatste item wijst.
        (vergemakkelijkt de implementatie van de queue)
        head : de headpointer, van klasse Head
        count : houdt het aantal items bij
        """
        self.head = Head()
        self.count = count

    def __del__(self):
        """
        Verwijdert de ketting.
        """
        del self

    def isEmpty(self):
        """
        Checkt of de ketting leeg is.
        :return: Geeft True indien de ketting leeg is,
                        False indien deze niet leeg is.
        """
        if self.count == 0:
            return True
        else:
            return False

    def getLength(self):
        """
        Geeft de lengte van de ketting
        :return: geeft self.count terug, hetgeen de lengte van de ketting bijhoud
        """
        return self.count

    def insert(self, index, item):
        """
        Voegt item toe aan de lijst, op de gegeven index. Deze index moet aan 1<=index<=count+1 voldoen om het item te kunnen toevoegen.
        :param index: de index die aangeeft waar het item toegevoegd moet worden.
        :param item: het item dat toegevoegd wordt
        :return: geeft True indien 1 <= index <= count + 1,
                        False als de index niet aan de vereisten voldoet.
        """
        if 1 <= index <= self.count + 1:
            if self.count == 0:     #laat item naar zichzelf wijzen, zodat als er een tweede item komt er een circulaire ketting gevormd kan worden
                self.head.next = item
                item.next = item
            if index == 1:      #speciaal geval waar de pointer van de head naar het nieuwe item moet wijzen
                firstItem = self.head.next
                item.next = firstItem.next
                firstItem.next = item
                self.head.next = item       #head moet naar het nieuwe item wijzen
            else:
                prev = self.head
                for teller in range(1, index):      #zoek de node die net op plaats index-1 staat
                    prev = prev.next
                item.next = prev.next
                prev.next = item
            self.count += 1
            return True
        else:
            return False

    def print(self):
        """
        Functie gebruikt om te testen. Het print alle items van de ketting.
        """
        current = self.head.next
        for i in range(0,self.count):
            print(current.item)
            current = current.next

    def retrieve(self, index):
        """
        Geeft item op plaatst index terug, als 1 <= index <= self.count.
        return: Een tuple met   False en None indien de lijst leeg is of de index niet aan de voorwaarde voldoet.
                                True en een item dat zich op plaats index bevindt.
        """
        if not 1 <= index <= self.count:
            return (False,None)
        if self.isEmpty() is True:
            return (False, None)

        current = self.head.next
        for teller in range(1, index):
            current = current.next
        return (True, current.item)

    def delete(self, index):
        """
        Verwijdert het item op plaats index als 1 <= index <= self.count.
        :param index: de plaats waar een item moet verwijderd worden
        :return: geeft  False terug als de index niet aan de voorwaarde voldoet of als de lijst leeg is
                        True terug als het verwijderen gelukt is.
        """
        if not 1 <= index <= self.count:    #de index moet waardig zijn
            return False
        if self.isEmpty() is True:      #als de lijst leeg is, kan je niet verwijderen
            return False
        if self.getLength() == 1:       #speciaal geval, nog maar 1 item, verwijder door self.head.next er niet meer naar te laten wijzen
            self.head.next = None
        if index == 1:      #als index == 1, dan moet dus het laatste item weg, dus moet men helemaal de ketting doorlopen om prev te vinden
            index = self.count + 1      #had evengoed range(0, index (zonder + 1)) kunnen doen, het doel is om naar het voorlaatste item te gaan
            current = self.head.next
            prev = self.head
            for teller in range(1, index):      #zoek 'voorlaatste' (eigenlijk laatste, maar visueel eerder 'voorlaatste' item, want deze wijst naar het laatste
                current = current.next
                prev = prev.next
            self.head.next = prev
            prev.next = current.next    #current moet eigenlijk weg, dus zetten we de pointer van de vorige op het item waar current naar wijst
                                        #op deze manier wordt current eigenlijk 'ovegeslagen'
        else:
            current = self.head.next
            prev = self.head
            for teller in range(1, index):
                current = current.next
                prev = prev.next
            prev.next = current.next


        self.count -= 1
        return True

    def bubblesort(self):
        pass


# 2-3 boom implementatie
# door Joke Duwaerts
# november 2017

import random


class _TreeItem:
    def __init__(self, item=None, key=None, next=None):
        self.item = item
        self.key = key
        self.next = next


class AdtTwoThreeTree:
    def __init__(self):
        """
        Een twoNode gebruikt rootLeft, parent, left, right en nodeType = 2
        Een threeNode gerbuikt rootLeft, rootRight, parent, left, midLeft, right en nodeType = 3
        Een tijdelijke fourNode gebruikt rootLeft, rootMid, rootRight, parent, left, midLeft, midRight, Right en nodeType = 4
        De regel is dat een _TreeItem steeds in rootLeft zal zitten bij een 2Node.
        """
        self.rootLeft = None
        self.rootRight = None
        self.rootMid = None
        self.left = None
        self.midLeft = None
        self.midRight = None
        self.right = None
        self.nodeType = 0
        self.parent = None

    def is_empty(self):
        """
        Kijkt na of de 23-boom leeg is. (leeg = geen kinderen)
        :return: Geeft een boolean  true terug als deze inderdaad leeg is.
                                    false terug als deze niet leeg is.
        """
        if self.right is None and self.left is None and self.midLeft is None and self.midRight is None:
            return True
        return False

    def table_is_empty(self):
        return self.rootLeft is None

    def destroy(self):
        """
        Maakt de 23-boom helemaal leeg. Omdat python zorgt voor het "opruimen" is het niet nodig alle treeItems en
        subbomen te verwijderen.
        """
        self.rootLeft = None
        self.rootRight = None
        self.left = None
        self.midLeft = None
        self.nodeType = 0
        self.right = None

    def compare_and_put_in_place(self, newItem):
        """
        Vergelijkt 'newItem' met de elementen in de knoop en plaats het op de juiste plaats in de root.
        :param newItem: het in te voegen item.
        :return: geeft een waarde terug, deze wordt gebruikt om bij 'split' te weten welke operaties juist moeten gebeuren.
        """
        if self.rootLeft is None:           # Als de knoop leeg is (geen kinderen, geen root),
            self.rootLeft = newItem         # plaats dan newItem in rootLeft
            return -1

        if self.nodeType == 2:                       # Als de knoop een 2-knoop is,
            # zet nodeType al op 3, want deze zal zo meteen een 3-knoop worden
            self.nodeType = 3
            # als de zoeksleutel van newItem kleiner is dan de zoeksleutel van
            # rootLeft,
            if self.rootLeft.key > newItem.key:
                # ... Verplaats dan het item in rootLeft naar rootRight,
                self.rootRight = self.rootLeft
                # ... zodat rootLeft kan ingenomen worden door newItem.
                self.rootLeft = newItem
                return 0
            else:                                       # als de zoeksleutel van newItem groter is dan de zoeksleutel van rootLeft,
                self.rootRight = newItem                # ... plaats dan newItem in rootRight
                return 1

        if self.nodeType == 3:                      # Als de knoop een 3-knoop is,
            # zet nodeType al op 4, want deze zal zo meteen een 4-knoop worden
            self.nodeType = 4
            # als de zoeksleutel van newItem kleiner is dan de zoeksleutels van
            # de root,
            if self.rootLeft.key > newItem.key:
                self.rootMid = self.rootLeft            # ... verplaats rootLeft naar rootMid,
                # ... zodat rootLeft kan ingenomen worden door newItem
                self.rootLeft = newItem
                # ... verplaats midLeft naar midRight zodat er plaats is voor twee nieuwe kinderen langs links.
                self.midRight = self.midLeft
                return 2
            # als de zoeksleutel kleiner is dan de grootste zoeksleutel van de
            # root,
            if self.rootRight.key > newItem.key:
                # ... plaats dan newItem in het midden (aka rootMid)
                self.rootMid = newItem
                return 3
            if self.rootRight.key < newItem.key:        # als de zoeksleutel groter is dan de zoeksleutels in de root,
                self.rootMid = self.rootRight           # ... verplaats rootRight naar rootMid,
                # ... zodat rootRIght ingenomen kan worden door newItem
                self.rootRight = newItem
                # self.midLeft = self.right               # ... verplaats het
                # rechterkind naar midLeft, zodat er plaats is voor twee nieuwe
                # kinder langs rechts
                return 4

    def split(self):
        """
        Splits de overvolle (knoop met 3 items) en zorgt dat er terug 2/3-knopen zijn.
        """
        wortelScenario = False              # Nodig om te bepalen of er een split bij de wortel wordt uitgevoerd of niet

        if self.parent is None:             # Als de node geen parent heeft,
            # maak dan een nieuwe knoop (twoThreeTree) genaamd pNode aan.
            pNode = AdtTwoThreeTree()
            wortelScenario = True
        else:                               # Anders,
            # als de node wel nog een parent heeft, dan is deze parent de
            # pNode.
            pNode = self.parent

        n1 = AdtTwoThreeTree()             # Maak twee nieuwe 2-3 bomen aan, n1 en n2
        n2 = AdtTwoThreeTree()
        # Plaats in n1 het linkerItem van de node en in n2 het rechterItem
        n1.insert(self.rootLeft)
        n2.insert(self.rootRight)
        n1.parent = pNode               # Maak pNode de ouder van n1 en n2
        n2.parent = pNode

        # Als de huidige node een interne knoop is, geen blad is:
        if not self.is_empty():
            # Plaats dan de twee linkerkinderen (left and midLeft) in n1
            n1.left = self.left
            n1.right = self.midLeft
            # Plaats de twee rechterkinderen (right and midRight) in n2
            n2.left = self.midRight
            n2.right = self.right
            # Zorg dat deze kinderen allemaal weten wat hun nieuwe ouder is (n1
            # of n2)
            n1.left.parent = n1
            n1.right.parent = n1
            n2.left.parent = n2
            n2.right.parent = n2

        # Plaats in de pNode de middelste root van de node
        result = pNode.compare_and_put_in_place(self.rootMid)
        # (deze moet naar boven worden gebracht en dus bij pNode komen)
        if result == -1:            # -1 : lege knoop (kinderen en root leeg)
            pNode.left = n1             # pNode krijgt n1 en n2 als resp. linker- en rechterkind
            pNode.right = n2
        elif result == 0:           # 0 : rootMid bevindt zich nu links in pNode, een 3-knoop
            pNode.left = n1             # pNode krijgt n1 en n2 als resp. linker en middelkind
            pNode.midLeft = n2
        elif result == 1:           # 1 : rootMid bevindt zich nu rechts in pNode, een 3-knoop
            pNode.midLeft = n1          # pNode krijgt n1 en n2 als resp. middel en rechterkind
            pNode.right = n2
        elif result == 2:           # 2 : rootMid bevindt zich nu links in pNode, een 4-knoop
            pNode.left = n1             # pNode krijgt n1 en n2 als resp. linker en linkermiddelkind
            pNode.midLeft = n2
        elif result == 3:           # 3 : rootMid bevindt zich nu in het midden in pNode, een 4-knoop
            # pNode krijgt n1 en n2 als resp. linkermiddel en rechtermiddelkind
            pNode.midLeft = n1
            pNode.midRight = n2
        else:                       # 4 : rootMid bevindt zich nu rechts in pNode, een 4-knoop
            # pNode krijgt n1 en n2 als resp. rechtermiddel en rechterkind
            pNode.midRight = n1
            pNode.right = n2

        if wortelScenario:          # Als er een nieuwe knoop werd aangemaakt omdat de huidige node de wortel was, gn parent had,
                                    # dan moet de huidige knoop alles van pNode
                                    # overnemen, omdat enkel zo men de nieuwe
                                    # boom kan bereiken via de huidige knoop.
            self.rootMid = None
            self.rootRight = None               # maak er terug helemaal een 2-knoop van
            self.nodeType = 2
            self.rootLeft = pNode.rootLeft      # neem de kinderen en rootItem over van pNode
            self.right = pNode.right
            self.left = pNode.left
            # Als de wortel nog een middelste kind zou hebben, moet deze
            # sowieso op None komen
            self.midLeft = None
            # zorg zeker dat de kinderen weten welk hun nieuwe parent is
            self.left.parent = self
            self.right.parent = self

        self.midRight = None

        # Als de pNode drie items blijkt te bevatten (alleen dan is rootMid
        # niet None)
        if not wortelScenario and pNode.nodeType == 4:
            # Voer hier dan ook de split op uit.
            pNode.split()

    def insert_item(self, key, item):
        """
        Voegt een nieuw item toe aan de boom, als de searchkey van dit item nog niet voorkomt.
        :param key:  De zoeksleutel van het item.
        :param item: Het item dat ingevoegd moet worden
        : return: bool die  true is als het item toegevoegd is.
                            false is als het item niet toegevoegd is (de searchkey kwam dus al voor).
        """
        self.insert(_TreeItem(item, key))

    def insert(self, newItem):
        """
        Voegt een nieuw item toe aan de boom, als de searchkey van dit item nog niet voorkomt.
        :param newItem: Het item dat ingevoegd moet worden
        : return: bool die  true is als het item toegevoegd is.
                            false is als het item niet toegevoegd is (de searchkey kwam dus al voor).
        """
        if self.nodeType == 0:              # Als de node leeg is,
            # plaats dan in de root (standaard is dit rootLeft) het newItem,
            self.rootLeft = newItem
            self.nodeType = 2               # het is een 2-knoop geworden
            return True                     # geef True terug, inserten gelukt
        if self.rootLeft.key == newItem.key:    # Als de zoeksleutel gelijk is aan de zoeksleutel in de rechterRoot, moet het item bij de ketting worden geplaatst
            newItem.next = self.rootLeft
            self.rootLeft = newItem
            return True
        if self.nodeType == 3:              # Als de node een 3-knoop is,
            if newItem.key == self.rootRight.key:  # en zoeksleutel al aanwezig is, voeg bij de ketting
                newItem.next = self.rootRight
                self.rootRight = newItem
                return True
            if self.is_empty():                              # Als de 3-knoop geen kinderen heeft,
                # plaats dan newItem erbij,
                self.compare_and_put_in_place(newItem)
                # En voer de split-functie uit, want er is nu een knoop met 4
                # items.
                return self.split()
            else:                                               # Als de 3-knoop wel kinderen heeft, zoek dan verder in
                # ...het linkerkind indien de zoeksleutel van newItem kleiner is dan de zoeksleutel van het kleinste item in de root
                if newItem.key < self.rootLeft.key:
                    return self.left.insert(newItem)            # zo niet:
                # ...het middenkind indien de zoeksleutel van newItem kleiner is dan de zoeksleutel van het grootste item in de root
                elif newItem.key < self.rootRight.key:
                    return self.midLeft.insert(newItem)         # zo niet:
                # ...het linkerkind als de zoeksleutel van newItem groter is dan de zoeksleutel van beide items in de root
                elif newItem.key > self.rootRight.key:
                    return self.right.insert(newItem)
        # Als de node een 2-knoop is...
        if self.nodeType == 2:
            if self.is_empty():                              # ... en de knoop is leeg,
                # plaats newItem in de knoop, en geef True terug.
                self.compare_and_put_in_place(newItem)
                return True
            elif self.rootLeft.key > newItem.key:
                # zoek dan verder in het rechterkind.
                return self.left.insert(newItem)
            else:
                return self.right.insert(newItem)

    def inorder_successor(self):
        """
        Geeft de subtree die als root de inorder successor heeft van de de gegeven subtree is. Deze subtree heeft niet als root het item waarvan men de inorder succ
        wilt vinden, maar is het juiste kind van de boom die het item wel bevat. (oftewel middel of rechter kind.)
        :param subtree: de correcte subtree van de (sub)tree waarin het item zit waarvan men de inorder successor wilt vinden.
        :return: geeft de subtree met de inorder successor terug.
        """
        if self.is_empty():
            return self
        else:
            return self.left.inorder_successor()

    def retrieve(self, key):
        """Zoekt een item met searchkey 'key' in de boom. Indien aanwezig, geeft het dit item, de (sub)tree waarin die zich
        bevind en een bepaalde waarde terug. Deze waarde wordt gebruikt om te weten of het item zich in de linker- of rechter-
        root van de subtree bevind.
        """
        if self.rootLeft is None and self.rootRight is None:
            return (None, None, 0)
        if key == self.rootLeft.key:                # Als de key gelijk is aan de zoeksleutel van root Left, kan al meteen
            # de node, subtree en waarde 1 (wilt zeggen: zit in rootLeft)
            # teruggeven worden
            return (self.rootLeft, self, 1)
        elif self.nodeType == 2:
            if self.is_empty():
                return (None, None, 0)
            elif key < self.rootLeft.key:
                return self.left.retrieve(key)
            else:
                return self.right.retrieve(key)
        elif self.nodeType == 3:                    # Als het een 3-knoop is
            if key == self.rootRight.key:           # en het is in de rootRight, dan kan deze worden teruggeven met waarde
                # 2 (wilt zeggen: zit in rootRight)
                return (self.rootRight, self, 2)
            elif self.is_empty():
                return (None, None, 0)
            elif key < self.rootLeft.key:
                return self.left.retrieve(key)
            elif key < self.rootRight.key:
                return self.midLeft.retrieve(key)
            else:
                return self.right.retrieve(key)
        elif self.is_empty():
            return (None, None, 0)

    def retrieve_item(self, key):
        """Zoekt een item met searchkey 'key' in de boom. Indien aanwezig, geeft het dit item, de (sub)tree waarin die zich
        bevind en een bepaalde waarde terug. Deze waarde wordt gebruikt om te weten of het item zich in de linker- of rechter-
        root van de subtree bevind.
        """
        if self.rootLeft is None and self.rootRight is None:
            return (None, False)
        if key == self.rootLeft.key:                # Als de key gelijk is aan de zoeksleutel van root Left, kan al meteen
            # de node, subtree en waarde 1 (wilt zeggen: zit in rootLeft)
            # teruggeven worden
            return (self.rootLeft.item, True)
        elif self.nodeType == 2:
            if self.is_empty():
                return (None, False)
            elif key < self.rootLeft.key:
                return self.left.retrieve_item(key)
            else:
                return self.right.retrieve_item(key)
        elif self.nodeType == 3:                    # Als het een 3-knoop is
            if key == self.rootRight.key:           # en het is in de rootRight, dan kan deze worden teruggeven met waarde
                # 2 (wilt zeggen: zit in rootRight)
                return (self.rootRight.item, True)
            elif self.is_empty():
                return (None, False)
            elif key < self.rootLeft.key:
                return self.left.retrieve_item(key)
            elif key < self.rootRight.key:
                return self.midLeft.retrieve_item(key)
            else:
                return self.right.retrieve_item(key)
        elif self.is_empty():
            return (None, False)

    def fix(self):
        """
        Deze functie voert het fix-algoritme uit. Dit is nodig wanneer bij de remove een lege node (subtree) ontstaat.
        In het kort: Als de sibling van de node een item te veel heeft, dan zal er een hele verschuiving plaatsvinden
        waarbij de lege node het (juiste) item van de ouder krijgt en de ouder het (juiste) van de sibling.
        Als de sibling geen item op overschot heeft, vindt er een merge plaats waarbij het (juiste) item in de ouder merged
        met de sibling. Bij dit geval is het mogelijk dat de ouder dan leeg is en dat er opnieuw het fix-algoritme moet worden uitgevoerd.
        OPMERKING: er moeten ook steeds kinderen worden verplaatst (bij bladen zijn dit dan lege kinderen)
        """
        # Ik zet het nodeType van de node op 2, omdat als de situatie zich voordoet dat de ouder zijn item doorgeeft aan de node
        # dat de node ook inderdaad als nodeType 2 heeft. (De node zal in het
        # geval er al een fix is geweest nodeType = 0 hebben.)
        self.nodeType = 2

        # Er moet gecheckt worden of er met de wortel van de boom of met een andere node wordt gewerkt. Dit wordt gecheckt via
        # de parent (die None is bij de wortel). Als het inderdaad de wortel is, die op het moment leeg is, moet deze worden verwijderd.
        # Verwijderen gaat echter niet bij de wortel, dus wordt alles (kinderen en rootItems) overgenomen van het kind. (Er nog maar
        # 1 kind over, want de lege wortel werd juist bekomen doordat het vorige fix algoritme de parent leegmaakte, waarbij er twee
        # lege nodes ontstonden. (de parent (in dit geval dus de wortel) en de
        # node waar het fix algoritme op werd toegepast)
        # De wortel is leeg, zorg ervoor dat alles wordt overgenomen van de
        # kinderen
        if self.parent is None:
            # Afhankelijk van welk kind niet leeg is, wordt alles overgenomen. De enigste opties zijn het rechter en linkerkind
            # want de node zou niet leeg zijn, moest het een middelste kind
            # hebben (da zou het een 3-knoop zijn met 2 linker en rechterroot)
            if self.right is None:
                self.rootLeft = self.left.rootLeft
                self.rootRight = self.left.rootRight
                self.nodeType = self.left.nodeType
                self.right = self.left.right
                self.midLeft = self.left.midLeft
                # Pas op het laatste moment het linkerkind door het linkerkind van het linkerkind vervangen, want anders zou
                # het linkerkind al verdwenen zijn, voordat alles is
                # overgenomen.
                self.left = self.left.left
            else:
                self.rootLeft = self.right.rootLeft
                self.rootRight = self.right.rootRight
                self.nodeType = self.right.nodeType
                self.left = self.right.left
                self.midLeft = self.right.midLeft
                # Ook hier pas op het laatste moment het kind zelf vervangen
                self.right = self.right.right

            # Zorgt ervoor dat de kinderen weten dat ze een nieuwe ouder hebben
            self.set_children_parent()
            return

        # Als de node een interne knoop is, dan kan het niet anders dan dat het maar 1 kind heeft (logica van het algoritme)
        # Om de implementatie te vergemakkelijken, zorg ik ervoor dat het
        # altijd nog het linkerkind heeft (dat bespaart if-statements).
        if self.left is None:           # Als het dus een rechterkind is, wordt dit verplaatst naar het linkerkind
            self.left = self.right
            self.right = None

        # Volgende grote brok code, houdt zich bezig met de nodige
        # verplaatsingen of merges in de verschillende gevallen

        # Als we werken met een kind dat een linkerkind is, moet er gecheckt worden of de ouder een 2-knoop of 3-knoop is
        # en of de sibling een 2-knoop of 3-knoop is.
        if self.parent.left == self:
            # De node heeft nu het item van de ouder, dit is NIET ALTIJD nodig
            self.rootLeft = self.parent.rootLeft

            # De ouder is een 2-knoop en de sibling een 3-knoop:
            # Er moet een verplaatsing gebeuren. Hierbij moet de sibling (het rechterkind) een 2-knoop worden. De roots
            # van de sibling moeten ook opgeschoven worden (om item in rootLeft te hebben en niet rootRight)
            # De node moet ook het linkerkind van de sibling krijgen, ook hier moet bij de sibling een verlaatsing, van de kinderen
            # plaatsvinden zodat deze enkel een linker- en rechterkind heeft.
            if self.parent.nodeType == 2 and self.parent.right.nodeType == 3:
                self.parent.rootLeft = self.parent.right.rootLeft
                self.parent.right.rootLeft = self.parent.right.rootRight
                self.parent.right.rootRight = None
                self.right = self.parent.right.left
                self.parent.right.left = self.parent.right.midLeft
                self.parent.right.midLeft = None
                self.parent.right.nodeType = 2

            # De ouder is een 3-knoop en sibling een 3-knoop. Dit volgt hetzelfde principe als hierboven, behalve dat er
            # nu moet gewerkt worden met het middelste kind van de ouder, niet
            # het rechterkind.
            elif self.parent.nodeType == 3 and self.parent.midLeft.nodeType == 3:
                self.right = self.parent.midLeft.left
                self.parent.midLeft.left = self.parent.midLeft.midLeft
                self.parent.midLeft.midLeft = None
                self.parent.rootLeft = self.parent.midLeft.rootLeft
                self.parent.midLeft.rootLeft = self.parent.midLeft.rootRight
                self.parent.midLeft.rootRight = None
                self.parent.midLeft.nodeType = 2

            # De ouder is een 2-knoop en sibling een 2-knoop. De sibling (rechterkind) heeft geen item op overschot, dus
            # er moet een merge plaatsvinden. Het item van de ouder komt bij de sibling (eerst moet rootLeft van de sibling
            # verplaatsen naar rootRight, zodat het item van de ouder erbij kan op de correctie plaats), de ouder is nu
            # leeg en krijgt als nodeType 0. De sibling krijgt daarintegen een nodeType = 3 (wordt een 3-knoop).
            # De kinderen moeten ook weer verplaatst worden. Linkerkind van de sibling wordt middelste kind, zodat er plaats
            # is voor het kind van de node (waar het algoritme wordt op uitgevoerd), dit kind is sowieso het linkerkind. (hier is
            # voor gezorgd, enkele lijnen terug)
            elif self.parent.nodeType == 2 and self.parent.right.nodeType == 2:
                self.parent.right.midLeft = self.parent.right.left
                self.parent.right.left = self.left
                self.parent.right.rootRight = self.parent.right.rootLeft
                self.parent.right.rootLeft = self.parent.rootLeft
                self.parent.rootLeft = None
                self.parent.nodeType = 0
                self.parent.right.nodeType = 3
                # De node verwijderen als kind van de (lege) ouder
                self.parent.left = None

            # Als de ouder een 3-knoop is en de sibling (middelste kind van ouder) een 2-knoop, dan wordt er eigenlijk een
            # heel boel verplaatst zodat de ouder een 2-knoop wordt met linkerkind de huidige node die een 3-knoop is geworden.
            # Hiervoor moet de rootRight van de huidige knoop de rootLeft van de sibling krijgen en ook de kinderen van de sibling
            # overnemen als midLeft en right kind. (die resp. het linker en
            # rechterkind waren)
            elif self.parent.nodeType == 3 and self.parent.midLeft.nodeType == 2:
                self.right = self.parent.midLeft.right
                self.midLeft = self.parent.midLeft.left
                self.rootRight = self.parent.midLeft.rootLeft
                self.parent.rootLeft = self.parent.rootRight
                self.parent.nodeType = 2
                self.nodeType = 3               # Belangrijk dat node als nodeType 3 krijgt
                # Ouder wordt een 2-knoop & alles is overgenomen van sibling,
                # dus sibling mag weg
                self.parent.midLeft = None

        # Als de node een rechterkind is van de ouder moeten acties van het zelfde principe worden uitgevoerd als bij de situatie
        # waar de node het linkerkind is.
        elif self.parent.right == self:

            # Ouder is 2-knoop en sibling (linkerkind van ouder) is 3-knoop. Dus er moeten items verplaatst worden. De huidige
            # node krijgt de rootLeft van de ouder, de ouder krijgt de rootRight van de sibling. De huidige node moet zijn linkerkind
            # verplaatsen naar het rechterkind zodat die het rechterkind van de sibling kan overnemen. De sibling moet zijn rechterkind
            # door zijn middelste kind vervangen en van nodeType 2 worden.
            if self.parent.nodeType == 2 and self.parent.left.nodeType == 3:
                self.rootLeft = self.parent.rootLeft
                # verplaatsen, voor het overnemen van het rechterkind van de
                # sibling
                self.right = self.left
                self.left = self.parent.left.right
                self.parent.left.right = self.parent.left.midLeft
                # sibling is 2-knoop geworden, midleft is al verplaatst, dus
                # zet op None
                self.parent.left.midLeft = None
                self.parent.rootLeft = self.parent.left.rootRight
                # sibling is 2-knoop geworden, rootRight is al overgenomen, dus
                # zet op None
                self.parent.left.rootRight = None
                self.parent.left.nodeType = 2

            # Ouder is 3-knoop en sibling (middelkind van ouder) is 3-knoop, geldt het zelfde principe als hierboven, er wordt
            # wel met het middelste kind van de ouder gewerkt, niet het
            # linkerkind.
            elif self.parent.nodeType == 3 and self.parent.midLeft.nodeType == 3:
                self.rootLeft = self.parent.rootRight
                self.right = self.left
                self.left = self.parent.midLeft.right
                self.parent.midLeft.right = self.parent.midLeft.midLeft
                self.parent.midLeft.midLeft = None
                self.parent.rootRight = self.parent.midLeft.rootRight
                self.parent.midLeft.rootRight = None
                self.parent.midLeft.nodeType = 2

            # Ouder is 2-knoop en sibling (linkerkind van ouder) is 2-knoop. Er moet een merge gebeuren. De root van de ouder komt bij de
            # sibling, als rootRight, en de ouder moet een nodeType 0 krijgen. De sibling wordt een 3-knoop en na het verplaatsen van
            # zijn rechterkind naar middelste kind, neemt het het linkerkind
            # van de huidige node over als rechterkind.
            elif self.parent.nodeType == 2 and self.parent.left.nodeType == 2:
                self.parent.left.midLeft = self.parent.left.right
                self.parent.left.right = self.left
                self.parent.left.rootRight = self.parent.rootLeft
                self.parent.rootLeft = None                         # ouder wordt een lege node
                self.parent.nodeType = 0
                self.parent.left.nodeType = 3
                # de huidige node mag verwijderd worden (op None zetten bij
                # ouder)
                self.parent.right = None

            # Ouder is een 3-knoop en sibling (middelste kind van ouder), hier wordt ongeveer hetzelfde gedaan als hierboven, alleen
            # wordt er nu met het middelste kind van de ouder gewerkt. De ouder wordt hier niet leeg, maar wel een 2-knoop.
            # Ook wordt het rechterkind van de ouder niet op None gezet, maar
            # juist vervangen door het middelste kind.
            elif self.parent.nodeType == 3 and self.parent.midLeft.nodeType == 2:
                self.parent.midLeft.midLeft = self.parent.midLeft.right
                self.parent.midLeft.right = self.left
                self.parent.midLeft.rootRight = self.parent.rootRight
                self.parent.nodeType = 2
                self.parent.midLeft.nodeType = 3
                self.parent.rootRight = None
                self.parent.right = self.parent.midLeft
                self.parent.midLeft = None

        # Als de node een middelste kind is van de ouder (alleen bij 3-knoop), zijn er nog twee situaties. (een vier, want
        # de situatie waar de ouder een 2-knoop is, is niet van toepassing.) Ik heb ervoor gekozen naar het rechterkind van de
        # ouder te kijken voor de sibling. (men zou ook het linkerkind genomen
        # kunnen hebben)
        elif self.parent.midLeft == self:
            # Als de sibling een 3-knoop is, dan moet de huidige knoop de rootRight van de ouder overnemen en het linkerkind van de sibling.
            # De sibling moet zijn middelste kind naar linkerkind verplaatsen en een 2-knoop worden, waarbij het middelste kind op
            # None wordt gezet. De rootRight van de ouder moet rootLeft van de sibling overnemen en vervolgens moet rootRight van de sibling
            # naar rootLeft verplaatsen, waarbij rootRight al meteen op None
            # wordt gezet. De sibling wordt een 2-knoop.
            if self.parent.right.nodeType == 3:
                self.right = self.parent.right.left
                self.parent.right.left = self.parent.right.midLeft
                self.parent.right.midLeft = None
                self.rootLeft = self.parent.rootRight
                self.parent.rootRight = self.parent.right.rootLeft
                self.parent.right.rootLeft = self.parent.right.rootRight
                self.parent.right.rootRight = None
                self.parent.right.nodeType = 2
            # Als de sibling een 2-knoop is, moet de rootRight van de ouder mergen met de sibling, waarbij de rootLeft eerst verplaatst
            # wordt naar rootRight. De sibling moet het kind van de huidige node overnemen als linkerkind, maar eerst moet
            # het linkerkind van de sibling naar het middelste kind verplaatsen.
            # De ouder wordt een 2-knoop en de sibling een 3-knoop. RootRight
            # van de ouder moet verwijderd worden en het middelste kind ook.
            elif self.parent.right.nodeType == 2:
                self.parent.right.midLeft = self.parent.right.left
                self.parent.right.left = self.left
                self.parent.right.rootRight = self.parent.right.rootLeft
                self.parent.right.rootLeft = self.parent.rootRight
                self.parent.right.nodeType = 3
                self.parent.rootRight = None
                self.parent.nodeType = 2
                self.parent.midLeft = None

        # Het volgende zorgt ervoor dat alle kinderen weten wat hun (nieuwe) ouder is. Laat u niet misleiden, set_children_parent()
        # zorgt ervoor dat de kinderen van node weten wat hun ouder is, de kinderen van self.parent worden niet op hun ouder gecheckt,
        # maar de kinderen van deze kinderen wel.
        if self.parent.left is not None:
            self.parent.left.set_children_parent()
        if self.parent.midLeft is not None:
            self.parent.midLeft.set_children_parent()
        if self.parent.right is not None:
            self.parent.right.set_children_parent()

        # Als de ouder leeg blijkt te zijn, moet het hele algoritme hier terug
        # op uitgevoerd worden.
        if self.parent.nodeType == 0:
            self.parent.fix()

    def remove(self, key):
        """
        Zoekt item met zoeksleutel 'key', als deze aanwezig is, wordt item verwijderd uit de boom.
        :param key: de zoeksleutel van het te verwijderen item
        :return: een boolean die aangeeft of het verwijderen gelukt is (false als de er geen item met zoeksleutel 'key' in de boom aanwezig is.
        """
        # Zoek het item met zoeksleutel 'key', retrieve geeft de node, subtree en een bepaald cijfer dat aangeeft waar
        # het item zich bevindt in de node.
        (node, subtree, numb) = self.retrieve(key)

        """ numb = 1 betekent dat het item zich in de --> linker root bevind
            numb = 2 betekent dat het item zich in de --> rechter root bevind """

        if node is None:        # Als node None is, was er dus geen item met zoeksleutel 'key' gevonden
            return False        # wordt er false teruggeven.

        # Als er meerdere items met de zoeksleutel aanwezig zijn, moet de hele node niet verwijderd worden, enkel 1 zo'n item
        # De root moet dus wijzen naar het volgende item in de linked list
        # (python doet het nodige verwijderen).
        if numb == 1 and subtree.rootLeft.next is not None:
            subtree.rootLeft = subtree.rootLeft.next
            return True
        if numb == 2 and subtree.rootRight.next is not None:
            subtree.rootRight = subtree.rootRight.next
            return True

        if self.parent is None and self.rootRight is None and self.is_empty(
        ):   # Als het item het enigste item is in de
            # hele boom, moet dit item gewoon weg
            self.rootLeft = None
            return True

        # Als het een blad is, dan moet in het geval van een 2-knoop het fix algoritme worden uitgevoerd, want de knoop
        # zal leeg achterblijven.
        # In het geval van een 3-knoop moet het item verwijderd worden, maar er moet rekening gehouden worden met de regel
        # dat een 2-knoop altijd een root in rootLeft heeft zitten.
        if subtree.is_empty():
            if numb == 1 and subtree.nodeType == 2:
                # node moet leeggemaakt worden (= item wordt verwijderd)
                subtree.rootLeft = None
                return subtree.fix()
            # Bij een 3-knoop en het item als rootLeft (numb = 1), moet rootLeft het item van rootRight krijgen
            # Omdat er gewerkt wordt met linked list, is er geen probleem bij dit verplaatsen van de item.
            # Belangrijk : nodeType wordt aangepast, want het wordt een 2-knoop
            elif numb == 1 and subtree.nodeType == 3:
                subtree.rootLeft = subtree.rootRight
                subtree.rootRight = None
                subtree.nodeType = 2
            # Als het item zich in de rechterRoot bevind, moeten we rootRight
            # op None zetten
            elif numb == 2:
                subtree.rootRight = None
                subtree.nodeType = 2

        else:   # Wanneer de knoop een interne knoop is, moet er met de inorder successor worden geswapt en vervolgens in de knoop
                # waar deze inorder successor zat verder gewerkt worden.
            # Als het item in rootLeft zit van een 3-knoop moet de inorder
            # succesor
            if numb == 1 and subtree.nodeType == 3:
                # in de middelste deelboom gezocht worden
                inordSuc = subtree.midLeft.inorder_successor()
            else:                                                   # In alle andere gevallen in de rechter deelboom
                inordSuc = subtree.right.inorder_successor()

            # een kopie zorgt ervoor dat de inorder successor niet "verloren" gaat. De inorder successor bevind zich sowieso in
            # rootLeft, want anders zou de hele essence van de inorder
            # successor teniet gaan.
            kopie = inordSuc.rootLeft
            if numb == 2:       # Het swappen van de inorder successor met het te-verwijderen-item als deze zich in rootRight bevind
                inordSuc.rootLeft = subtree.rootRight
                subtree.rootRight = kopie
                # remove moet nu op de originele subtree van de inorder
                # successor worden toegepast
                return inordSuc.remove(key)
            # Het swappen als het te-verwijderen-item zich in rootLeft bevind
            # (voor 2-knoop en 3-knoop)
            else:
                inordSuc.rootLeft = subtree.rootLeft
                subtree.rootLeft = kopie
                return inordSuc.remove(key)

    def set_children_parent(self):
        """
        Zorgt ervoor dat de kinderen van de tree als parent de tree zelf hebben. Dit kan nodig zijn bij het verwijderen,
        wanneer kinderen van ouder verwisselen.
        :return:
        """
        if self.left is not None:
            self.left.parent = self
        if self.midLeft is not None:
            self.midLeft.parent = self
        if self.right is not None:
            self.right.parent = self

    def print_inorder(self):
        """
        Print de items (zoeksleutels om makkelijk te zien of het juist is) volgens gesorteerde searchkey volgorde.
        :return:
        """
        if self.rootLeft is None:       # Als de node geen rootLeft heeft, dan is deze leeg. Dit geval kan enkel bij een lege wortel bereikt worden.
            print("Empty tree, nothing to print.")
            return
        if self.is_empty():              # Als de node geen kinderen heeft, wordt het item/worden de items in de node geprint
            print(self.rootLeft.key)
            if self.nodeType == 3:      # Als het een 3-knoop is, heeft de node een rechteritem, dit moet ook geprint worden
                print(self.rootRight.key)
            return
        if self.nodeType == 2:          # Als het een 2-knoop is, die niet leeg is, dan moet print_inorder van de 2 kinderen gedaan
                                        # worden volgens de logische volgorde
                                        # van inorer traverse. Het item in de
                                        # node moet ook geprint worden
            self.left.print_inorder()
            print(self.rootLeft.key)
            self.right.print_inorder()
        if self.nodeType == 3:          # Als het een 3-knoop is, die niet leeg is, dan moet print_inorder van de 3 kinderen gedaan
                                        # worden volgens de logische volgorde
                                        # van inorder traverse. De items in de
                                        # node moeten ook geprint worden.
            self.left.print_inorder()
            print(self.rootLeft.key)
            self.midLeft.print_inorder()
            print(self.rootRight.key)
            self.right.print_inorder()

    def create_dot_file(self, filename):
        """
        Maakt een dotfile aan van de huidige boom.
        : filename  :   De naam die aan de .dot file gegeven wordt.
        """
        # dotFile is de nieuwe file, (met bestandsnaam 'filename', en deze
        # staat op 'w' want we willen de file aanpassen
        dotFile = open(filename, 'w')

        # volgend stukje voegt aan dotFile de standaard lijnen code voor het maken van de graph die 'tree' noemt.
        # de node, edge en graph lijnen zorgen voor de layout en zijn dus niet noodzakelijk... Maar wie heeft er nu niet
        # liever een matrix-thema voor de boom ipv het standaard thema? :)
        dotFile.write("digraph tree {")
        dotFile.write(
            "\n" +
            'node [shape=Mrecord, style=filled, fillcolor="#34373d", fontcolor="#1aba4a", fontname=Ubuntu, compound=true, color="#1aba4a"];')
        dotFile.write("\n" + 'edge [color="#1aba4a"];')
        dotFile.write("\n" + 'graph [rankdir=TD, bgcolor="#34373d"];')

        # Enkel als de boom niet volledig leeg is kan er met de add_node_to_file
        # functie gewerkt worden:
        if self.rootLeft is not None:
            # de add_node_to_file functie zal de nodige nodes en edges toevoegen
            # aan 'dotFile'
            self.add_node_to_file(dotFile)
        dotFile.write("\n" + "}")

    def add_node_to_file(self, file):
        """
        De functie die het werkelijke werk doet voor het maken van de .dot file. Het voegt de nodes en edges toe.
        :param file: de file waarin gewerkt wordt
        """
        leftKey = str(
            self.rootLeft.key)                 # leftKey is een string van de zoeksleutel van rootLeft, het liet me toe niet steeds str te doen
        # nodeName zal de naam van de node worden, steeds rootLeft, want deze
        # is altijd aanwezig
        nodeName = "node" + str(self.rootLeft.key)
        """
        RANDINFORMATIE: voor de personen die niet bekend zijn met records in de DOT language:
        Er wordt gewerkt met records om meerdere elementen in 1 node te krijgen, de notatie in DOT voor een record node is:
        bv: nodeNaam [label=" Rick | Morty "];                --> met twee aparte elementen (Rick en Morty) aangegeven door "|"
        er zou ook echt werkelijk labels gegeven kunnen worden, zodat je kan beslissen vanuit welk deeltje je een pijl wilt laten vertrekken
        bv. nodeNaam [label="<f0> Rick | <f1> Morty];         --> en dan zou je bv een edge kunnen doen: nodeNaam:f0 --> andereNode:f1
        Ik heb niet met de speciefieke labels gewerkt, omdat dit mij heel wat code zou besparen en dit niet nodig was
        (de code in zo'n volgorde is dat alles al goed komt te staan).
        """
        # Als de node leeg is (gn kinderen), dan moet de node zelf wel nog worden aangemaakt via de syntax die hierboven is aangehaald
        # Hoe deze wordt aangemaakt hangt af van of het een 2-knoop of 3-knoop is. De naam is echter enkel afhankelijk van de linkerRoot
        # en is dus in beide gevallen gelijk.
        if self.is_empty():
            if self.nodeType == 2:
                file.write("\n" + nodeName + ' [label=" ' + leftKey + '"];')
            else:
                file.write("\n" +
                           nodeName +
                           ' [label=" ' +
                           leftKey +
                           '| ' +
                           str(self.rootRight.key) +
                           '"];')

        # Als het een niet-lege 2-knoop is, moet de functie ook bij de 2 kinderen worden toegepast en de node zelf moet
        # ook aangemaakt worden.
        elif self.nodeType == 2:
            file.write("\n" + nodeName + ' [label=" ' + leftKey + '"];')
            self.left.add_node_to_file(file)
            self.right.add_node_to_file(file)

        # Als het een niet-lege 3-knoop is, moet de functie ook bij de 3 kinderen worden toegepast en de node zelf moet
        # ook aangemaakt worden.
        elif self.nodeType == 3:
            file.write("\n" +
                       nodeName +
                       ' [label=" ' +
                       leftKey +
                       '| ' +
                       str(self.rootRight.key) +
                       '"];')
            self.left.add_node_to_file(file)
            self.midLeft.add_node_to_file(file)
            self.right.add_node_to_file(file)

        # Als de node een parent heeft, dan moet er een edge tussen deze twee komen (een pijl van parent naar node),
        # de node van de parent is al aangemaakt (de recursieve oproepen starten vanaf de root) en de naam van deze
        # node werd bepaald door de key van de linkerRoot, dus deze kunnen we
        # terugvinden als "node" + str(key parent)
        if self.parent is not None:
            if self.parent.rootLeft is None:
                print("error: ", self.rootLeft.key)
            nameParent = "node" + str(self.parent.rootLeft.key)
            # edge van parent naar node, dus eerst parent dan node
            file.write("\n" + nameParent + " -> " + nodeName + ";")


"""
Webpagina's die ik heb geraadpleegd om de .DOT file te maken.
- Node Shapes, geraadpleegd op 5/12/2017 via http://www.graphviz.org/doc/info/shapes.html
- Node, Edge and Grapgh Attributes. Geraadpleegd op 5/12/2017 via http://www.graphviz.org/doc/info/attrs.html
"""

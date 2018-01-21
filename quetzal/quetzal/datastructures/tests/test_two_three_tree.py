from unittest import TestCase
from quetzal import *
import random
from datetime import datetime

class TestTwoThreeTree(TestCase):
    def test_empty(self):
        tree = AdtTwoThreeTree()
        self.assertTrue(tree.is_empty())
        tree.__setitem__(5, "5")
        self.assertFalse(tree.is_empty())
        tree.__setitem__(6, "6")
        tree.__setitem__(8, "8")
        tree.__setitem__(7, "7")
        tree.__setitem__(9, "9")
        self.assertFalse(tree.is_empty())

    def test_retrieve(self):
        tree = AdtTwoThreeTree()
        tree.__setitem__(3, "3")
        tree.__setitem__(9, "9")
        tree.__setitem__(3, "3")
        tree.__setitem__(3, "3")
        tree.__setitem__(5, "5")
        tree.__setitem__(6, "6")
        tree.__setitem__(12, "12")
        tree.__setitem__(14, "14")

        # keys's present in tree
        self.assertTrue(tree.__contains__(3))
        self.assertTrue(tree.__contains__(5))
        self.assertTrue(tree.__contains__(12))
        self.assertTrue(tree.__contains__(14))
        self.assertTrue(tree.__contains__(9))
        self.assertTrue(tree.__contains__(6))

        # key's present not in tree
        self.assertFalse(tree.__contains__(8))
        self.assertFalse(tree.__contains__(10))
        self.assertFalse(tree.__contains__(17))
        self.assertFalse(tree.__contains__(55))
        self.assertFalse(tree.__contains__(0))
        self.assertFalse(tree.__contains__(4))


def genereer_23(aantal):
    """
    Deze functie maakt een boom aan met 'aantal' TreeItems.
    :param aantal: geeft het aantal TreeItems.
    :return: geeft een TwoThreeTree terug.
    """
    lijstMetTreeItems = list()
    for i in range(aantal):
        lijstMetTreeItems.append(i)       # Invoegen TreeItems met zoeksleutel 'i' en item de string van 'i'
    tree = AdtTwoThreeTree()
    size = aantal                                           # Bepaalt hoe veel keer de loop wordt gedaan
    for i in range(size):
        random.seed(datetime.now())
        randomInLijst = random.randint(0, aantal - 1)
        item = lijstMetTreeItems[randomInLijst]
        del lijstMetTreeItems[randomInLijst]


        tree.__setitem__(item, str(item))
        aantal -= 1                         # Aantal = aantal - 1, omdat er 1 TreeItem minder in de lijst is, zodat de randomwaarde
                                            # in de volgende loop in het juiste interval wordt gekozen
    tree.__repr__()
    return tree

def removing_23(tree, aantal):
    """
    Verwijderd alle TreeItems, behalve 1 uit de boom. Er wordt 1 overgelaten om te checken of alles zeker oké is.
    :param tree:    De 23-boom waarvan men de TreeItems gaat verwijderen.
    :param aantal:  Het aantal items in de 'tree'.
    """
    # Een lijst wordt aangemaakt met hierin: 1,2,...,aantal
    lijstMetKeys = list()
    for i in range(aantal):
        lijstMetKeys.append(i)

    while not tree._no_children():
        random.seed(datetime.now())
        randomInLijst = random.randint(0, aantal - 1)
        key = lijstMetKeys[randomInLijst]
        tree.__delitem__(key)
        tree.__repr__()     # extra check of the "relationship" between children and parent (and vice versa)

tree = genereer_23(200)
removing_23(tree, 200)
from unittest import TestCase
from ..datastructures import *
import random
from datetime import datetime

class TestBsTree(TestCase):
    def test_empty(self):
        tree = AdtBinarySearchTree()
        self.assertTrue(tree.is_empty())
        tree.__setitem__(5, "5")
        self.assertFalse(tree.is_empty())
        tree.__setitem__(8, "8")
        self.assertFalse(tree.is_empty())

    def test_retrieve(self):
        tree = AdtBinarySearchTree()
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

        self.assertEqual(3,tree.__getitem__(3)[1].key)
        self.assertEqual(5,tree.__getitem__(5)[1].key)
        self.assertEqual(12,tree.__getitem__(12)[1].key)
        self.assertEqual(14,tree.__getitem__(14)[1].key)
        self.assertEqual(9,tree.__getitem__(9)[1].key)
        self.assertEqual(6,tree.__getitem__(6)[1].key)

        # key's present not in e
        self.assertFalse(tree.__contains__(8))
        self.assertFalse(tree.__contains__(10))
        self.assertFalse(tree.__contains__(17))
        self.assertFalse(tree.__contains__(55))
        self.assertFalse(tree.__contains__(0))
        self.assertFalse(tree.__contains__(4))

def genereer_bst(aantal):
    """
    Deze functie maakt een boom aan met 'aantal' TreeItems.
    :param aantal: geeft het aantal TreeItems.
    :return: geeft een TwoThreeTree terug.
    """

    lijstCijfers = list()
    for i in range(aantal):
        lijstCijfers.append(i)       # Invoegen TreeItems met zoeksleutel 'i' en item de string van 'i'
    tree = AdtBinarySearchTree()
    size = aantal                                           # Bepaalt hoe veel keer de loop wordt gedaan
    for i in range(size+(int(size/2))):
        random.seed(datetime.now())                         # Om ervoor te zorgen dat de seed steeds veranderd naargelang de tijd
        randomInLijst = random.randint(0, aantal - 1)       # RandomInLijst is de index voor de lijst die random werd gekozen
        item = lijstCijfers[randomInLijst]                  # item is nu het TreeItem dat op de random index in LijstMetTreeItems zat
        tree.__setitem__(item, str(item))                        # Het TreeItems plaatsen in de boom
    tree.__repr__()
    return tree

def removing_bst(tree, aantal):
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
        tree.__repr__()

a = genereer_bst(200)
removing_bst(a, 200)
from unittest import TestCase
from datastructures import *
import random
from datetime import datetime

class TestBsTree(TestCase):
    def test_empty(self):
        tree = AdtBinarySearchTree()
        self.assertTrue(tree.is_empty())
        tree[5] = "5"
        self.assertFalse(tree.is_empty())
        tree[8] = "8"
        self.assertFalse(tree.is_empty())

    def test_retrieve(self):
        tree = AdtBinarySearchTree()
        tree[3] = "3"
        tree[9] = "9"
        tree[3] = "3"
        tree[3] = "3"
        tree[5] = "5"
        tree[6] = "6"
        tree[12] = "12"
        tree[14] = "14"

        # keys's present in tree
        self.assertTrue(3 in tree)
        self.assertTrue(9 in tree)
        self.assertTrue(5 in tree)
        self.assertTrue(6 in tree)
        self.assertTrue(12 in tree)
        self.assertTrue(14 in tree)

        # key's present not in tree
        self.assertFalse(8 in tree)
        self.assertFalse(10 in tree)
        self.assertFalse(17 in tree)
        self.assertFalse(55 in tree)
        self.assertFalse(0 in tree)
        self.assertFalse(4 in tree)

    def test_delete(self):
        tree = AdtBinarySearchTree()
        tree[1] = "1"
        tree[2] = "2"
        tree[28] = "28"
        tree[0] = "0"
        tree[19] = "19"
        tree[11] = "11"

        self.assertTrue(1 in tree)
        del tree[1]
        self.assertFalse(1 in tree)
        self.assertTrue(28 in tree)
        del tree[28]
        self.assertFalse(28 in tree)
        self.assertTrue(11 in tree)
        del tree[11]
        self.assertFalse(11 in tree)

    def test_duplicate(self):
        tree = AdtBinarySearchTree()
        tree[5] = "5.1"
        tree[6] = "6.1"
        tree[5] = "5.2"
        tree[5] = "5.3"
        tree[2] = "2.1"
        tree[2] = "2.2"

        self.assertEqual(tree[5], "5.1")
        self.assertEqual(tree[6], "6.1")
        del tree[5]
        self.assertEqual(tree[5], "5.2")
        del tree[5]
        self.assertEqual(tree[5], "5.3")
        self.assertEqual(tree[2], "2.1")
        del tree[2]
        self.assertEqual(tree[2], "2.2")
        del tree[2]
        self.assertIsNone(tree[2])

    def test_fuzzing(self, aantal=200):
        tree = AdtBinarySearchTree()
        lijst = genereer(tree, aantal)
        for i in range(int(aantal/4)):
            random.seed(datetime.now())
            randomInLijst = random.randint(0, len(lijst) - 1)
            key = lijst[randomInLijst]
            self.assertTrue(key in tree)
            del tree[key]
            self.assertFalse(key in tree)
            del lijst[randomInLijst]

        raised = False
        try:
            tree2 = AdtBinarySearchTree()
            genereer(tree2, 200)
            removing(tree2, 200)
        except:
            raised = True
        self.assertFalse(raised)


def genereer(tree, N):
    """ Inserts 90% of numbers from zero to N in the given tree.

    :param aantal: geeft het aantal TreeItems.
    :return: geeft een TwoThreeTree terug.
    """
    lijstMetTreeItems = []
    secondLijst = []
    for i in range(N):
        lijstMetTreeItems.append(i)       # Invoegen TreeItems met zoeksleutel 'i' en item de string van 'i'
    size = N                                           # Bepaalt hoe veel keer de loop wordt gedaan
    for i in range(N):
        random.seed(datetime.now())
        randomInLijst = random.randint(0, N - 1)
        item = lijstMetTreeItems[randomInLijst]
        secondLijst.append(item)
        del lijstMetTreeItems[randomInLijst]
        tree[item] = str(item)
        N -= 1

    return secondLijst

def removing(tree, aantal):
    """
    Verwijderd alle TreeItems, behalve 1 uit de boom. Er wordt 1 overgelaten om te checken of alles zeker oké is.
    :param tree:    De 23-boom waarvan men de TreeItems gaat verwijderen.
    :param aantal:  Het aantal items in de 'tree'.
    """
    # Een lijst wordt aangemaakt met hierin: 1,2,...,aantal
    lijstMetKeys = list()
    for i in range(aantal):
        lijstMetKeys.append(i)

    while not tree._no_children() and not len(lijstMetKeys) == 0:
        random.seed(datetime.now())
        randomInLijst = random.randint(0, len(lijstMetKeys) - 1)
        key = lijstMetKeys[randomInLijst]
        del tree[key]
        del lijstMetKeys[randomInLijst]
        repr(tree)     # extra check of the "relationship" between children and parent (and vice versa)

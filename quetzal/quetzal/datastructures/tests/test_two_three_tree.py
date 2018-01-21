from unittest import TestCase
from datastructures import *
import random
from datetime import datetime

class TestTwoThreeTree(TestCase):
    def test_empty(self):
        tree = AdtTwoThreeTree()
        self.assertTrue(tree.is_empty())
        tree[3] = "3"
        self.assertFalse(tree.is_empty())
        tree[3] = "3"
        tree[9] = "9"
        tree[3] = "3"
        tree[3] = "3"
        self.assertFalse(tree.is_empty())

    def test_retrieve(self):
        tree = AdtTwoThreeTree()
        tree[3] = "3"
        tree[9] = "9"
        tree[3] = "3"
        tree[3] = "3"
        tree[5] = "5"
        tree[6] = "6"
        tree[12] = "12"
        tree[14] = "14"

        # keys present in tree
        self.assertTrue(3 in tree)
        self.assertTrue(9 in tree)
        self.assertTrue(5 in tree)
        self.assertTrue(6 in tree)
        self.assertTrue(12 in tree)
        self.assertTrue(14 in tree)

        # keys not present in tree
        self.assertFalse(8 in tree)
        self.assertFalse(10 in tree)
        self.assertFalse(17 in tree)
        self.assertFalse(55 in tree)
        self.assertFalse(0 in tree)
        self.assertFalse(4 in tree)

    def test_delete(self):
        tree = AdtTwoThreeTree()
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
        tree = AdtTwoThreeTree()
        tree[5] = "5.1"
        tree[6] = "6.1"
        tree[5] = "5.2"
        tree[5] = "5.3"
        tree[2] = "2.1"
        tree[2] = "2.2"

        self.assertEqual(tree[5], "5.3")
        self.assertEqual(tree[6], "6.1")
        del tree[5]
        self.assertEqual(tree[5], "5.2")
        del tree[5]
        self.assertEqual(tree[5], "5.1")
        self.assertEqual(tree[2], "2.2")
        del tree[2]
        self.assertEqual(tree[2], "2.1")
        del tree[2]
        self.assertIsNone(tree[2])

    def test_fuzzing(self, aantal=200):
        tree = AdtTwoThreeTree()
        lijst = genereer(tree, aantal)
        for i in range(int(aantal/4)):
            random.seed(datetime.now())
            randomInLijst = random.randint(0, len(lijst) - 1)
            item = lijst[randomInLijst]
            self.assertTrue(item in tree)
            del tree[item]
            self.assertFalse(item in tree)
            del lijst[randomInLijst]

        raised = False
        try:
            tree2 = AdtTwoThreeTree()
            genereer(tree2, 200)
            removing(tree2, 200)
        except:
            raised = True
        self.assertFalse(raised)

def genereer(tree, N):
    """ Inserts 90% of numbers from zero to N in the given tree.

    :param N: Number of items that should be inserted in the tree.
    :param tree: The tree in which the items will be inserted.
    :return: geeft een TwoThreeTree terug.
    """
    lijstMetTreeItems = []
    secondLijst = []
    for i in range(N):
        lijstMetTreeItems.append(i)       
    size = N                              
    for i in range(int(N*(9/10))):
        random.seed(datetime.now())
        randomInLijst = random.randint(0, N - 1)
        item = lijstMetTreeItems[randomInLijst]
        secondLijst.append(item)
        del lijstMetTreeItems[randomInLijst]
        tree[item] = str(item)
        N -= 1

    return secondLijst

def removing(tree, N):
    """ Deletes all items but one from the tree. During this deletion the dot-string method is called. This way the
    structure of the tree is checked.

    :param tree:    The tree from which the elements will be deleted.
    :param N:  The number of items in this tree.
    """
    lijstMetKeys = list()
    for i in range(N):
        lijstMetKeys.append(i)

    while not tree._no_children() and not len(lijstMetKeys) == 0:
        random.seed(datetime.now())
        randomInLijst = random.randint(0, len(lijstMetKeys) - 1)
        key = lijstMetKeys[randomInLijst]
        del tree[key]
        del lijstMetKeys[randomInLijst]
        repr(tree)     # extra check of the "relationship" between children and parent (and vice versa)

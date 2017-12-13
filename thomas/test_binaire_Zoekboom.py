from unittest import TestCase
from Binaire_Zoekboom import Binaire_Zoekboom

class TestBinaire_Zoekboom(TestCase):
    def test_isEmpty(self):
        tree = Binaire_Zoekboom()
        self.assertTrue(tree.isEmpty())
        tree.searchTreeInsert(5, "test")
        self.assertFalse(tree.isEmpty())

    def test_searchTreeInsert(self):
        tree = Binaire_Zoekboom()
        root = tree.searchTreeInsert(5, "test")
        tree.searchTreeInsert(3, "test2", root)
        tree.searchTreeInsert(7, "test3", root)
        tree.searchTreeInsert(6, "test4", root)
        self.assertFalse(tree.isEmpty())
        self.assertEqual(3, root.leftSubTree.key)
        self.assertEqual(7, root.rightSubTree.key)
        self.assertEqual(6, root.rightSubTree.leftSubTree.key)

    def test_searchTreeRetrieve(self):
        tree = Binaire_Zoekboom()
        root = tree.searchTreeInsert(5, "test")
        tree.searchTreeInsert(3, "test2", root)
        tree.searchTreeInsert(7, "test3", root)
        tree.searchTreeInsert(6, "test4", root)
        self.assertEqual(root, tree.searchTreeRetrieve(5))
        self.assertEqual(root.leftSubTree, tree.searchTreeRetrieve(3))
        self.assertEqual(root.rightSubTree, tree.searchTreeRetrieve(7))
        self.assertEqual(root.rightSubTree.leftSubTree, tree.searchTreeRetrieve(6))

    def test_print(self):
        tree = Binaire_Zoekboom()
        root = tree.searchTreeInsert(5, "test")
        tree.searchTreeInsert(3, "test2", root)
        tree.searchTreeInsert(7, "test3", root)
        tree.searchTreeInsert(6, "test4", root)
        tree.print()
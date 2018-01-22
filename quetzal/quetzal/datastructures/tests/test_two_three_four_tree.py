from datastructures import *
from unittest import TestCase

class TestTwoThreeFourTree(TestCase):
    def test_init_and_delete(self):
        t = AdtTwoThreeFourTree()
        self.assertTrue(t.is_empty())
        self.assertEqual(t.root, None)
        t[0] = 45
        t[1] = 10
        self.assertFalse(t.is_empty())
        self.assertNotEqual(t.root, None)

    def test_insert(self):
        t = AdtTwoThreeFourTree()
        t[10] = "10a"
        t[10] = "10b"
        t[60] = "60"
        t[10] = "10c"
        self.assertFalse(t.is_empty())
        t[30] = "30"
        t[40] = "40"
        self.assertEqual(t.root.amount, 1)
        t[70] = "70"
        self.assertEqual(t.root.amount, 1)
        t[90] = "90"
        self.assertEqual(t.root.amount, 2)
        self.assertEqual(t.root.children[0].amount, 1)
        self.assertEqual(t.root.children[1].amount, 1)
        self.assertEqual(t.root.children[2].amount, 2)
        self.assertEqual(t.root.children[3], None)








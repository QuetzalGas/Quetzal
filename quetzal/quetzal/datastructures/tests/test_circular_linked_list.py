from datastructures import *
from unittest import TestCase


class TestCircularLinkedList(TestCase):
    def testInitandDelete(self):
        lst = AdtCircularLinkedList()
        self.assertEqual(lst.head, lst.dummy_head)
        self.assertEqual(lst.dummy_head.next, lst.dummy_head)
        lst[1] = "abc"
        lst.__del__()
        self.assertEqual(lst.head, lst.dummy_head)
        self.assertEqual(lst.dummy_head.next, lst.dummy_head)

    def testEmpty(self):
        lst = AdtCircularLinkedList()
        self.assertTrue(lst.is_empty())
        lst[0] = "abc"
        self.assertFalse(lst.is_empty())
        lst[1] = "def"
        lst[2] = "ghi"
        self.assertFalse(lst.is_empty())
        lst.__del__()
        self.assertTrue(lst.is_empty())

    def testGetLength(self):
        lst = AdtCircularLinkedList()
        self.assertEqual(lst.get_length(), 0)
        lst[0] = "abc"
        self.assertEqual(lst.get_length(), 1)
        lst[1] = "def"
        lst[2] = "ghi"
        self.assertEqual(lst.get_length(), 3)
        lst.__del__()
        self.assertEqual(lst.get_length(), 0)

    def testInsert(self):
        lst = AdtCircularLinkedList()
        lst[0] = 10
        lst[1] = 0
        lst[2] = 5
        with self.assertRaises(TypeError):
            lst[3] = "abc"
        lst[3] = 7
        with self.assertRaises(KeyError):
            lst[10] = 5
        lst[4] = -57
        self.assertEqual(lst.get_length(), 5)

    def testDelete(self):
        lst = AdtCircularLinkedList()
        lst[0] = 10
        lst[1] = 0
        lst[2] = 5
        lst[3] = 7
        del lst[2]
        del lst[1]
        self.assertEqual(lst.get_length(), 2)
        with self.assertRaises(KeyError):
            del lst[10]
        with self.assertRaises(KeyError):
            del lst[3]
        del lst[1]
        del lst[0]
        self.assertTrue(lst.is_empty())

    def testGet(self):
        lst = AdtCircularLinkedList()
        lst[0] = 10
        lst[1] = 0
        lst[2] = 5
        lst[3] = 7
        self.assertEqual(lst[1], 0)
        self.assertEqual(lst[0], 10)
        self.assertEqual(lst[2], 5)
        self.assertEqual(lst[3], 7)
        with self.assertRaises(KeyError):
            test = lst[4]
        del lst[2]
        self.assertEqual(lst[2], 7)
        with self.assertRaises(KeyError):
            test1 = lst[3]

    def testContains(self):
        lst = AdtCircularLinkedList()
        lst[0] = 10
        lst[1] = 0
        lst[2] = 5
        lst[3] = 7
        self.assertTrue(10 in lst)
        self.assertTrue(0 in lst)
        self.assertTrue(5 in lst)
        self.assertTrue(7 in lst)
        self.assertFalse(8 in lst)
        del lst[2]
        self.assertFalse(5 in lst)
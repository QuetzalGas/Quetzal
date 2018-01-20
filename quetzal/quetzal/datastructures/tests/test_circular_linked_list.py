from quetzal import *
from unittest import TestCase

class TestCircularLinkedList(TestCase):
    def testInitandDelete(self):
        l = AdtCircularLinkedList()
        self.assertEqual(l.head, l.dummy_head)
        self.assertEqual(l.dummy_head.next, l.dummy_head)
        l.insert(1, "abc")
        l.__del__()
        self.assertEqual(l.head, l.dummy_head)
        self.assertEqual(l.dummy_head.next, l.dummy_head)

    def testEmpty(self):
        l = AdtCircularLinkedList()
        self.assertTrue(l.is_empty())
        l.insert(1, "abc")
        self.assertFalse(l.is_empty())
        l.insert(2, "def")
        l.insert(3, "ghi")
        self.assertFalse(l.is_empty())
        l.__del__()
        self.assertTrue(l.is_empty())

    def testIsEmpty(self):
        l = AdtCircularLinkedList()
        self.assertEqual(l.get_length(), 0)
        l.insert(1, "abc")
        self.assertEqual(l.get_length(), 1)
        l.insert(2, "def")
        l.insert(3, "ghi")
        self.assertEqual(l.get_length(), 3)
        l.__del__()
        self.assertEqual(l.get_length(), 0)

    def testInsert(self):
        l = AdtCircularLinkedList()

    def testDelete(self):
        pass

    def testGet(self):
        pass


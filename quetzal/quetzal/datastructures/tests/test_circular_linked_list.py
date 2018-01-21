from datastructures import *
from unittest import TestCase

class TestCircularLinkedList(TestCase):
    def test_init_and_delete(self):
        l = AdtCircularLinkedList()
        self.assertEqual(l.head, l.dummy_head)
        self.assertEqual(l.dummy_head.next, l.dummy_head)
        l[0] = "abc"
        l.__del__()
        self.assertEqual(l.head, l.dummy_head)
        self.assertEqual(l.dummy_head.next, l.dummy_head)

    def test_empty(self):
        l = AdtCircularLinkedList()
        self.assertTrue(l.is_empty())
        l[0] = "abc"
        self.assertFalse(l.is_empty())
        l[1] = "def"
        l[2] = "ghi"
        self.assertFalse(l.is_empty())
        l.__del__()
        self.assertTrue(l.is_empty())

    def test_is_empty(self):
        l = AdtCircularLinkedList()
        self.assertEqual(len(l), 0)
        l[0] = "abc"
        self.assertEqual(len(l), 1)
        l[1] = "def"
        l[2] = "ghi"
        self.assertEqual(len(l), 3)
        l.__del__()
        self.assertEqual(len(l), 0)

    def test_init(self):
        l = AdtCircularLinkedList()
        self.assertTrue(l.head == l.dummy_head)
        self.assertTrue(l.dummy_head.next == l.dummy_head)

    def test_is_empty_2(self):
        l = AdtCircularLinkedList()
        self.assertTrue(l.is_empty())
        l[0] = "abc"
        self.assertFalse(l.is_empty())
        l[1] = "def"
        l[2] = "ghi"
        self.assertFalse(l.is_empty())
        del l[0]
        del l[1]
        del l[0]
        self.assertTrue(l.is_empty())


    def test_len(self):
        l = AdtCircularLinkedList()
        self.assertEqual(0, len(l))
        l[0] = "abc"
        self.assertEqual(1, len(l))
        l[1] = "def"
        l[2] = "ghi"
        self.assertEqual(3, len(l))
        del l[0]
        del l[1]
        self.assertEqual(1, len(l))
        del l[0]
        self.assertEqual(0, len(l))

    def test_insert(self):
        l = AdtCircularLinkedList()
        with self.assertRaises(IndexError):
            l[1] = "abc"
        with self.assertRaises(IndexError):
            l[-1] = "def"
        l[0] = "abc"
        l[1] = "ghi"
        l[1] = "def"
        with self.assertRaises(IndexError):
            l[4] = "abc"
        self.assertEqual(3, len(l))
        with self.assertRaises(TypeError):
            l[2] = 6
        l[1] = "d"
        l[4] = "jkl"
        self.assertEqual(5, len(l))

    def test_insert_and_delete(self):
        l = AdtCircularLinkedList()
        l[0] = 0
        l[1] = 5
        l[2] = 7
        l[3] = -56
        del l[2]
        self.assertEqual(-56, l[2])
        self.assertEqual(3, len(l))
        l[2] = 30
        self.assertEqual(30, l[2])
        self.assertEqual(-56, l[3])
        del l[0]
        with self.assertRaises(IndexError):
            del l[10]
        with self.assertRaises(IndexError):
            del l[-1]
        self.assertEqual(3, len(l))

    def test_retrieve(self):
        l = AdtCircularLinkedList()
        l[0] = 0
        l[1] = 5
        l[2] = 7
        l[3] = -56
        with self.assertRaises(IndexError):
            x = l[-1]
        self.assertEqual(5, l[1])
        with self.assertRaises(IndexError):
            x = l[4]
        self.assertEqual(0, l[0])
        self.assertEqual(7, l[2])
        self.assertEqual(-56, l[3])
        del l[0]
        self.assertEqual(5, l[0])
        self.assertEqual(7, l[1])
        self.assertEqual(-56, l[2])
        self.assertEqual(3, len(l))
        with self.assertRaises(IndexError):
            x = l[3]
        del l[1]
        self.assertEqual(5, l[0])
        self.assertEqual(-56, l[1])
        with self.assertRaises(IndexError):
            x = l[2]
        self.assertEqual(2, len(l))



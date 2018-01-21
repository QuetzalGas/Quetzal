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

    def testInitandDelete(self):
        lst = AdtCircularLinkedList()
        self.assertEqual(lst.head, lst.dummy_head)
        self.assertEqual(lst.dummy_head.next, lst.dummy_head)
        lst[0] = "abc"
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
        self.assertEqual(len(lst), 0)
        lst[0] = "abc"
        self.assertEqual(len(lst), 1)
        lst[1] = "def"
        lst[2] = "ghi"
        self.assertEqual(len(lst), 3)
        lst.__del__()
        self.assertEqual(len(lst), 0)

    def testInsert(self):
        lst = AdtCircularLinkedList()
        lst[0] = 10
        lst[1] = 0
        lst[2] = 5
        with self.assertRaises(TypeError):
            lst[3] = "abc"
        lst[3] = 7
        with self.assertRaises(IndexError):
            lst[10] = 5
        lst[4] = -57
        self.assertEqual(len(lst), 5)

    def testDelete(self):
        lst = AdtCircularLinkedList()
        lst[0] = 10
        lst[1] = 0
        lst[2] = 5
        lst[3] = 7
        del lst[2]
        del lst[1]
        self.assertEqual(len(lst), 2)
        with self.assertRaises(IndexError):
            del lst[10]
        with self.assertRaises(IndexError):
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
        with self.assertRaises(IndexError):
            test = lst[4]
        del lst[2]
        self.assertEqual(lst[2], 7)
        with self.assertRaises(IndexError):
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

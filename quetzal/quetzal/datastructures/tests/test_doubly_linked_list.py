from datastructures import *
from unittest import TestCase


class TestDoublyLinkedList(TestCase):
    def test_destroyList(self):
        lst = AdtDoublyLinkedList()
        lst[0] = 5
        lst[1] = 7
        lst.__del__()
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)
        self.assertEqual(lst.length, 0)

    def test_isEmpty(self):
        lst = AdtDoublyLinkedList()
        self.assertTrue(lst.is_empty())
        lst._insert_beginning(5)
        self.assertFalse(lst.is_empty())

    def test_getLength(self):
        lst = AdtDoublyLinkedList()
        self.assertEqual(len(lst), 0)
        lst._insert_beginning(0)
        self.assertEqual(len(lst), 1)
        lst[1] = 5
        self.assertEqual(len(lst), 2)

    def test_insertBeginning(self):
        lst = AdtDoublyLinkedList()
        lst._insert_beginning(7)
        lst._insert_beginning(8)
        self.assertEqual(8, lst.head.item)
        self.assertEqual(7, lst.tail.item)
        lst._insert_beginning(9)
        self.assertEqual(9, lst.head.item)

    def test_insertEnd(self):
        lst = AdtDoublyLinkedList()
        lst._insert_beginning(7)
        self.assertEqual(7, lst.head.item)
        lst._insert_end(9)
        self.assertEqual(7, lst.head.item)
        self.assertEqual(9, lst.tail.item)

    def test_insertLocation(self):
        lst = AdtDoublyLinkedList()
        lst[0] = 3
        lst[1] = 5
        with self.assertRaises(IndexError):
            lst[3] = 7
        self.assertEqual(lst.head.item, 3)
        self.assertEqual(lst.tail.item, 5)
        lst[1] = 9
        self.assertEqual(lst.tail.item, 5)
        self.assertEqual(len(lst), 3)
        lst[0] = 12
        self.assertEqual(lst.head.item, 12)
        self.assertEqual(len(lst), 4)

    def test_delete(self):
        lst = AdtDoublyLinkedList()
        lst[0] = 5
        lst[1] = 7
        lst[0] = 6
        self.assertEqual(lst.head.item, 6)
        self.assertEqual(lst.tail.item, 7)
        lst[3] = 8
        self.assertEqual(lst.tail.item, 8)
        del lst[0]
        self.assertEqual(lst.head.item, 5)
        self.assertEqual(len(lst), 3)
        del lst[2]
        self.assertEqual(lst.tail.item, 7)
        self.assertEqual(len(lst), 2)
        with self.assertRaises(IndexError):
            del lst[3]

    def test_get(self):
        lst = AdtDoublyLinkedList()
        lst[0] = 5
        lst[1] = 7
        lst[0] = 6
        self.assertEqual(lst[0], 6)
        self.assertEqual(lst[1], 5)
        self.assertEqual(lst[2], 7)
        lst[2] = 8
        self.assertEqual(lst[3], 7)
        del lst[1]
        self.assertEqual(lst[1], 8)
        with self.assertRaises(KeyError):
            test = lst[5]

    def test_searchNode(self):
        lst = AdtDoublyLinkedList()
        lst[0] = 5
        lst[1] = 7
        lst[0] = 6
        self.assertTrue(5 in lst)
        self.assertTrue(7 in lst)
        self.assertTrue(6 in lst)
        self.assertFalse(9 in lst)
        del lst[2]
        self.assertFalse(7 in lst)

    def test_insert2(self):
        lst = AdtDoublyLinkedList()
        lst[0] = "test"
        lst[1] = "test2"
        self.assertTrue("test2" in lst)
        self.assertTrue("test" in lst)
        self.assertFalse("test3" in lst)

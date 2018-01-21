from quetzal import *
from unittest import TestCase


class TestDoublyLinkedList(TestCase):
    def test_destroyList(self):
        list = AdtDoublyLinkedList()
        list.insertBeginning(5)
        list.insertLocation(1, 7)
        list.destroyList()
        self.assertTrue(list.isEmpty())

    def test_isEmpty(self):
        list = AdtDoublyLinkedList()
        self.assertTrue(list.isEmpty())
        list.insertBeginning(5)
        self.assertFalse(list.isEmpty())

    def test_getLength(self):
        list = AdtDoublyLinkedList()
        list.insertBeginning(5)
        list.insertLocation(1, 7)
        self.assertEqual(2, list.getLength())
        list.retrieve(1)
        self.assertEqual(1, list.getLength())

    def test_insertLocation(self):
        list = AdtDoublyLinkedList()
        list.insertLocation(0, 8)
        list.insertLocation(0, 7)
        self.assertEqual(7, list.retrieve(0)[0])

    def test_insertBeginning(self):
        list = AdtDoublyLinkedList()
        list.insertBeginning(7)
        list.insertBeginning(8)
        self.assertEqual(8, list.retrieve(0)[0])

    def test_insertEnd(self):
        list = AdtDoublyLinkedList()
        list.insertEnd(7)
        self.assertEqual(7, list.retrieve(0)[0])
        list.insertEnd(9)
        self.assertEqual(7, list.retrieve(0)[0])
        self.assertEqual(9, list.retrieve(1)[0])

    def test_delete(self):
        list = AdtDoublyLinkedList()
        list.insertBeginning(7)
        list.insertEnd(8)
        list.insertEnd(9)
        list.insertBeginning(6)
        list.delete(2)
        self.assertEqual(9, list.retrieve(2)[0])

    def test_retrieve(self):
        list = AdtDoublyLinkedList()
        list.insertBeginning(5)
        list.insertBeginning(8)
        self.assertEqual(5, list.retrieve(1)[0])

    def test_searchNode(self):
        list = AdtDoublyLinkedList()
        list.insertBeginning(5)
        list.insertEnd(8)
        list.insertEnd(9)
        self.assertEqual(9, list.searchNode(2).item)
        self.assertEqual(8, list.searchNode(1).item)
        self.assertEqual(8, list.retrieve(1)[0])
        self.assertEqual(5, list.retrieve(0)[0])
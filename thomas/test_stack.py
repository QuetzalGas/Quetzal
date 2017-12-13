from unittest import TestCase
from Stack import Stack


class TestStack(TestCase):
    def test_createStack(self):
        stack = Stack()
        stack.createStack()
        self.assertIsNone(stack.top)

    def test_destroyStack(self):
        stack = Stack()
        stack.createStack()
        stack.push(5)
        stack.push(9)
        stack.destroyStack()
        self.assertIsNone(stack.top)

    def test_isEmpty(self):
        stack = Stack()
        stack.createStack()
        self.assertTrue(stack.isEmpty())
        stack.push(9)
        self.assertFalse(stack.isEmpty())
        stack.destroyStack()
        self.assertTrue(stack.isEmpty())

    def test_push(self):
        stack = Stack()
        stack.createStack()
        stack.push(5)
        self.assertFalse(stack.isEmpty())

    def test_pop(self):
        stack = Stack()
        stack.createStack()
        stack.push(8)
        stack.pop()
        self.assertTrue(stack.isEmpty())

    def test_getTop(self):
        stack = Stack()
        stack.createStack()
        stack.push(3)
        self.assertEqual(3, stack.getTop())
        stack.push(7)
        self.assertEqual(7, stack.getTop())
        stack.pop()
        self.assertEqual(3, stack.getTop())

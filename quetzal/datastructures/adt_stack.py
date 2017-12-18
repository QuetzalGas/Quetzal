class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class AdtStack:
    def createStack(self):
        """
        Creates a new stack.
        """
        self.top = None

    def destroyStack(self):
        """
        Destroys a stack.
        """
        self.top = None

    def isEmpty(self):
        """
        Indicates whether a stack is empty.
        :return: Boolean: If the top of the linked list has a top or not.
        """
        return self.top is None

    def push(self, newItem):
        """
        Pushes a new item onto the stack.
        :param newItem: The item that needs to be added to the stack
        :return: If it succeeded.
        """
        newNode = Node(newItem, self.top)
        self.top = newNode
        return True

    def pop(self):
        """
        Removes the last added element.
        :return: Whether the removal succeeded
        """
        if self.top is None:
            return False
        self.top = self.top.next
        return True

    def popAndReturn(self):
        """
        Removes the last added element and returns it.
        :return: The last added element.
        :return: Wether the removal succeeded.
        """
        if self.top is None:
            return False
        old_top = self.top
        self.top = self.top.next
        return old_top, True

    def getTop(self):
        """
        Indicates what the last added element is.
        :return: The last added element
        """
        return self.top.item


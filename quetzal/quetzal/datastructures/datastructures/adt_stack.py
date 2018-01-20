class _Node:
    def __init__(self, item, next_):
        self.item = item
        self.next = next_

class AdtStack:
    def __init__(self):
        """
        Creates a new stack.
        """
        self.top = None

    def destroy_stack(self):
        """
        Destroys a stack.
        """
        self.top = None

    def is_empty(self):
        """
        Indicates whether a stack is empty.
        :return: Boolean: If the top of the linked list has a top or not.
        """
        return self.top is None

    def push(self, item):
        """
        Pushes a new item onto the stack.
        :param newItem: The item that needs to be added to the stack
        :return: If it succeeded.
        """
        self.top = _Node(item, self.top)
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

    def pop_and_return(self):
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

    def get_top(self):
        """
        Indicates what the last added element is.
        :return: The last added element
        """
        return self.top.item

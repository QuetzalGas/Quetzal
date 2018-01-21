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

    def __del__(self):
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
        :raise TypeError if type of new item doesn't correspond with type of
        items already in stack
        """
        if not self.is_empty():
            if not isinstance(item, type(self.top.item)):
                raise TypeError
        self.top = _Node(item, self.top)

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
        :raise StopIteration if stack is empty.
        """
        if self.top is None:
            raise StopIteration

        old_top = self.top.item
        self.top = self.top.next
        return old_top

    def peek(self):
        """
        Indicates what the last added element is.
        :return: The last added element
        """
        if not self.is_empty():
            return self.top.item
        else:
            return None

    def __repr__(self):
        string = "digraph G {\ngraph [\nrankdir = \"LR\"\n];"
        if not self.is_empty():
            string += "\n\n\"node\" [\nlabel = \""
            cur = self.top
            string += str(cur.item)
            string += "|"
            while cur.next is not None:
                cur = cur.next
                string += str(cur.item)
                string += "|"
            string = string.strip("|")
            string += "\"\nshape = \"record\"\n];"
        string += "\n}"
        return string

class _Node:
    def __init__(self, item, prev, next):
        """ Creates new node.

        :param item: Item that contains data.
        :param prev: Previous node.
        :param next:  Next node.
        """
        self.item = item
        self.prev = prev
        self.next = next


class AdtDoublyLinkedList:
    def __init__(self):
        """
        Creates a new doubly linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def __del__(self):
        """
        Destroys the current double linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        """ Checks if a list is empty.

        :return: Boolean: If the list is empty or not.
        """
        return self.length == 0

    def __len__(self):
        """ Returns the length of the list

        :return: The length of the list
        """
        return self.length

    def __setitem__(self, index, new_item):
        """ Inserts a node into a given location.

        :param index: The index to insert into
        :param new_item: The item to insert
        :raise: KeyError if the index is not correct.
        """
        if not self.is_empty():
            if not isinstance(new_item, type(self.head.item)):
                raise TypeError
        if self.head is None or index == 0:
            self._insert_beginning(new_item)
        elif index == self.length:
            self._insert_end(new_item)
        elif not 0 <= index <= self.length:
            raise IndexError("Index out of range!")
        else:
            current_node = self._search_node(index - 1)
            new_node = _Node(new_item, current_node, current_node.next)
            # Correct the prev from the node after the current node
            current_node.next.prev = new_node
            # Correct the next from the current node
            current_node.next = new_node
            self.length += 1

    def _insert_beginning(self, new_item):
        """ Inserts a node at the beginning of the list.

        :param new_item: The item to insert into the list.
        """
        new_node = _Node(new_item, None, self.head)
        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def _insert_end(self, new_item):
        """ Inserts a node at the end of the list.

        :param new_item: The item to insert into the list.
        """
        last_node = self.tail
        new_node = _Node(new_item, last_node, None)
        last_node.next = new_node
        self.tail = new_node
        self.length += 1

    def __delitem__(self, index):
        """ Deletes a node from the list.

        :param index: The index of the node that needs to be removed
        :raise: KeyError if the index is incorrect.
        """
        if not 0 <= index < self.length:
            raise IndexError("Index out of range!")

        deleted_node = self._search_node(index)
        before_node = deleted_node.prev
        after_node = deleted_node.next

        if index == 0:
            self.head = after_node
        if index == self.length - 1:
            self.tail = before_node
        if before_node is not None:
            before_node.next = after_node
        if after_node is not None:
            after_node.prev = before_node
        self.length -= 1

    def __getitem__(self, index):
        """ Get a node from the list and returns the data from the node.

        :param index: The index of the node that needs to be retrieved
        :return: The retrieved item
        :raise: KeyError if the index is incorrect.
        """
        if not 0 <= index < self.length:
            raise KeyError("Index out of range!")

        found_node = self._search_node(index)
        return found_node.item

    def __contains__(self, item):
        """ Checks if the list contains a node with a given item.

        :param item: The item to search for.
        :return: True if the item is in the list, false otherwise.
        """
        current_node = self.head
        while current_node is not None:
            if current_node.item == item:
                return True
            current_node = current_node.next
        return False

    def _search_node(self, index):
        """ Searches the location of the node on the given index.

        :param index: The index of the node to search.
        :return: The found node.
        """
        i = 0
        current_node = self.head
        while i < index:
            current_node = current_node.next
            i += 1
        return current_node

    def __repr__(self):
        """ Creates the dot-representation of the list

        :return: string with dot-representation
        """
        string = "digraph dll {\ngraph [\nrankdir = \"LR\"\n];\n\n"
        for i in range(len(self)):
            string += str(i)
            string += " [\nlabel = \""
            string += str(i)
            string += ": "
            string += str(self[i])
            string += "\"\nshape = \"record\"\n];\n\n"
        for i in range(len(self)):
            string += str(i)
            string += " -> "
        string = string.strip(" -> ")
        string += "\n"
        for i in range(len(self)-1,-1,-1):
            string += str(i)
            string += " -> "
        string = string.strip(" -> ")
        string += "\n}"
        return string

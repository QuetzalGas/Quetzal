class Double_Node:
    def __init__(self, item, prev, next):
        self.item = item
        self.prev = prev
        self.next = next

class AdtDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def destroyList(self):
        """
        Destroys the current double linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        """
        Checks if a list is empty.
        :return: Boolean: If the list is empty or not.
        """
        if self.length == 0:
            return True
        else:
            return False


    def getLength(self):
        """
        Returns the length of the list
        :return: Integer
        """
        return self.length


    def insert(self, index, newItem):
        """
        Inserts a node into a given location.
        :param index: The index to insert into
        :param newItem: The item to insert
        :return: Boolean: If the insertion succeeded
        """
        if self.head is None or index <= 1:
            return self.insertBeginning(newItem)
        elif index > self.length:
            return self.insertEnd(newItem)
        else:
            current_node = self.searchNode(index-1)
            new_node = Double_Node(newItem, current_node, current_node.next)
            #Correct the prev from the node after the new node
            current_node.next.prev = new_node
            #Correct the next from the node before the new node
            current_node.next = new_node
            self.length += 1
            return True

    def insertBeginning(self, newItem):
        """
        Inserts a node at the beginning of the list.
        :param newItem: The item to insert
        :return: Boolean: If the insertion succeeded
        """
        new_node = Double_Node(newItem, None, self.head)
        if self.head is not None:
            self.head.prev = new_node
            self.tail = self.head
        self.head = new_node
        self.length += 1
        return True

    def insertEnd(self, newItem):
        """
        Inserts a node at the end of the list.
        :param newItem: The item to insert
        :return: Boolean: If the insertion succeeded
        """
        if self.head is None:
            return self.insertBeginning(newItem)
        else:
            last_node = self.searchNode(self.length-1)
            new_node = Double_Node(newItem, last_node, None)
            last_node.next = new_node
            self.tail = new_node
            self.length += 1
            return True

    def delete(self, index):
        """
        Deletes a node from the list.
        :param index: The index of the node that needs to be removed
        :return: Boolean: If the insertion succeeded
        """
        if index < 1:
            index = 1
        if index > self.getLength():
            index = self.getLength()
        deleted_node = self.searchNode(index)
        before_node = deleted_node.prev
        after_node = deleted_node.next
        if index == 1:
            self.head = after_node
        if before_node is not None:
            before_node.next = after_node
        if after_node is not None:
            after_node.prev = before_node
        self.length -= 1
        return True

    def retrieve(self, index):
        """
        Deletes a node from the list and returns the data from the node.
        :param index: The index of the node that needs to be retrieved
        :return: The retrieved item
        :return: Boolean: If the insertion succeeded
        """
        if index < 1:
            index = 1
        if index > self.getLength():
            index = self.getLength()
        deleted_node = self.searchNode(index)
        before_node = deleted_node.prev
        after_node = deleted_node.next
        if index == 1:
            self.head = after_node
        if before_node is not None:
            before_node.next = after_node
        if after_node is not None:
            after_node.prev = before_node
        self.length -= 1
        return deleted_node.item, True

    def searchNode(self, index):
        """
        Searches the location of the node just before the given index.
        :param index: The index of the node to search
        :return: The found node
        """
        i = 0
        current_node = self.head
        while i < index - 1:
            current_node = current_node.next
            i += 1
        return current_node

    def searchItem(self, index):
        result = self.searchNode(index)
        if result is None:
            return None, False
        else:
            return result.item, True
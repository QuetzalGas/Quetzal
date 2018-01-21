class _TreeItem:
    def __init__(self, key, item):
        self.item = item
        self.key = key

class AdtBinarySearchTree:
    def __init__(self, root=None):
        self.root = []
        if not root is None:
            self.root.append(root)
        self.left = None
        self.right = None
        self.parent = None

    def destroy(self):
        self.root = None
        self.right = None
        self.left = None

    def _no_children(self):
        """ Checks whether the tree has children or not.

        :return: True if it doesn't have any children, False otherwise.
        """
        if (self.left is None) and (self.right is None):
            return True
        else:
            return False

    def is_empty(self):
        """ Checks whether the tree is completely empty (no children and empty root).

        :return: True if the root is empty, False otherwise.
        """
        return len(self.root) == 0

    def __setitem__(self, key, item):
        """ Interface to insert a treeElement with 'key' as searchkey and 'item' as content.

        :param key: The searchkey of the new node.
        :param item: The contents of the new node.
        :raise: If key or item is of incorrect type, an exception is raised.
        """
        if not self.is_empty():
            if not isinstance(key, type(self.root[0].key)) or not isinstance(item, type(self.root[0].item)):
                raise TypeError("Unable to set item: key and.or item of incorrect type!")

        self._search_tree_insert(_TreeItem(key, item))

    def _search_tree_insert(self, item):
        """ Adds 'item' to the tree.

        :param item: Item is the object to be inserted. It is of type _TreeItem.
        """
        # If the tree is completely empty, item must be added to it's root.
        if self.is_empty() and self.parent is None:
            self.root.append(item)
            return

        # If here, item's key must be compared to the root's keys. Depending on the result:
        # * a new BST must be made for the item.
        # * the search must continue in one of the children.
        # * the item must be added to the root (same searchkey).
        if item.key < self.root[0].key:
            if self.left is None:
                self.left = AdtBinarySearchTree(item)
                self.left.parent = self
                return
            else:
                return self.left._search_tree_insert(item)
        elif item.key > self.root[0].key:
            if self.right is None:
                self.right = AdtBinarySearchTree(item)
                self.right.parent = self
                return
            else:
                return self.right._search_tree_insert(item)

        if item.key == self.root[0].key:
            self.root.append(item)
            return

    def __getitem__(self, key):
        """ Interface to the actual _retrieve() method. This method returns the node, not the subtree.

        :param key: The searchkey of which a node is searched.
        :return: (False, None) if there is no node with the searchkey == 'key', (True, node) otherwise.
        :raise : If key is of incorrect type, an exception is raised.
        """
        if not self.is_empty():
            if not isinstance(key, type(self.root[0].key)):
                raise TypeError("Unable to get item: key of incorrect type!")

        subtree = self._retrieve(key)[1]
        if subtree is None:
            return False, None
        return True, subtree.root[0]

    def __contains__(self, key):
        """ Interface to the actual _retrieve() method. This method returns a bool.

        :param key: The searchkey of which a node is searched.
        :return: False if there is no node with the searchkey == 'key', True otherwise.
        """
        return self._retrieve(key)[0]

    def _retrieve(self, key):
        """ Retrieves an item with the given searchkey.

        :param key: The searchkey of which a node is searched.
        :raise: If the given 'key' is of incorrect type, an exception is raised.
        :return: (False, None) if there is no node with the searchkey == 'key', (True, subtree) otherwise.
        """
        if len(self.root) == 0 and (self.parent is None):       # if the whole tree is empty, false is returned
            return (False, None)
        # If here, the key is compared to the key of the root. If they are not equal and the tree has children/a child,
        # the search will continue in a child.
        if key < self.root[0].key and self.left is not None:
            return self.left._retrieve(key)
        elif key > self.root[0].key and self.right is not None:
            return self.right._retrieve(key)
        if key == self.root[0].key:
            return (True, self)
        else:
            return (False, None)

    def _inorder_successor(self, right_child):
        """ Returns the inorder successor. Important: the subtree with which this method is called is always the right
        subtree of the (sub)tree of which we search the inorder successor. This enables the method to search to the most
        left node.

        :param right_child: The right subtree of the node of which the inorder successor is searched.
        :return: The subtree containing the inorder successor.
        """
        # As long as there is a left child, the search will continue. If the tree has no left child, it's root is the
        # inorder successor.
        if right_child.left is not None:
            return self._inorder_successor(right_child.left)
        else:
            return right_child

    def _act_remove(self):
        """ Removes a node in a recursively, which is the reason for it being a seperate function from __delitem__().
        """
        if self.parent:     # Making sure the node is deleted from it's parent's children.
            if self._no_children() is True:
                if self.parent.left == self:
                    self.parent.left = None
                else:
                    self.parent.right = None

        # If there is only one child, transfer the root and it's children to this (sub)tree.
        if (self.left is None) and self.right:
            self.root = self.right.root
            self.left = self.right.left
            self.right = self.right.right
        elif (self.right is None) and self.left:
            self.root = self.left.root
            self.right = self.left.right
            self.left = self.left.left
        # If there are two children, swap places with the inorder successor and carry this function out on that subtree.
        if self.left and self.right:
            inorderSucc = self._inorder_successor(self.right)
            self.root = inorderSucc.root
            inorderSucc._act_remove()

        # The possibly moved children should of this (sub)tree should know that this is their parent.
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __delitem__(self, key):
        """ Checks whether a node with the given 'key' is present, if so the remove will be carried out.

        :param key: The searchkey of the node to be deleted.
        :return: True if there was a node with searchkey == 'key', False otherwise.
        """
        if not self.is_empty():
            if not isinstance(key, type(self.root[0].key)):
                raise TypeError("Unable to delete item: key of incorrect type!")

        (bool, subtree) = self._retrieve(key)

        if bool is False:           # There is no node with the given key.
            return False
        if len(subtree.root) > 1:   # If there are multiple items with the given searchkey
            subtree.root.pop()
            return True
        else:
            return subtree._act_remove()

    def __repr__(self):
        """ The base method for creating a string that represents the dot-code.

        :return: A string containing the dot-code to create a graph.
        :raise: If the tree is empty, an exception is raised.
        """
        if self.is_empty():
            raise KeyError("Unable to create a dot-string of an empty tree!")
        string = "digraph bst {\nnode [shape=Mrecord];\n"
        string += self._get_string()
        string += "}"
        return string

    def _get_string(self):
        """ Makes the .dot string of the whole tree. It returns the current string, which is used not only outside this
        method. Inside this method each string of the children is added to the current one, if this tree has children.

        :return: A string containing all information of the nodes and the edges.
        """
        root_name = "node" + str(self.root[0].key)
        string = root_name + ' [label="'
        size_root = len(self.root)
        for i in range(0, size_root):
            string += self.root[i].item
            if i < size_root-1:
                string += ", "
        string += '"];\n'

        if self.right and self.left:
            string += self.left._get_string()
            string += self.right._get_string()
        if not self.left and self.right:
            invis = "inv" + str(self.root[0].key) + "left"
            string += invis + ' [style="invisible"];\n'
            string += root_name + ' -> ' + invis + " [style=invis];\n"
            string += self.right._get_string()
        if not self.right and self.left:
            self.left._get_string()
            invis = "inv" + str(self.root[0].key) + "right"
            string += invis + ' [style="invisible"];\n'
            string += root_name + ' -> ' + invis + " [style=invis];\n"

        if self.parent :
            string += "node" + str(self.parent.root[0].key) + " -> " + root_name + ";\n"
        return string
class _TreeItem:
    def __init__(self, key, item):
        if item is None:
            self.node_content = None
        else:
            self.node_content = [item]
        self.key = key

class AdtBinarySearchTree:
    def __init__(self, root=None):
        self.contents = root
        self.left = None
        self.right = None
        self.parent = None

    def __del__(self):
        self.contents = None
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
        """ Checks whether the tree is completely empty (no children and no contents).

        :return: True if the (sub)tree has no contents, False otherwise.
        """
        return self.contents is None

    def __setitem__(self, key, item):
        """ Interface to insert a treeElement with 'key' as searchkey and 'item' as content.

        :param key: The searchkey of the new node.
        :param item: The contents of the new node.
        :raise: If key or item is of incorrect type, an exception is raised.
        """
        if not self.is_empty():
            if not isinstance(key, type(self.contents.key)) or not isinstance(item, type(self.contents.node_content[0])):
                raise TypeError("Unable to set item: key and/or item of incorrect type!")

        self._search_tree_insert(_TreeItem(key, item))

    def _search_tree_insert(self, item):
        """ Adds 'item' to the tree.

        :param item: Item is the object to be inserted. It is of type _TreeItem.
        """
        # If the tree is completely empty, item must be added as it's content.
        if self.is_empty() and self.parent is None:
            self.contents = item
            return

        # If here, item's key must be compared to the content's key. Depending on the result:
        # * a new BST must be made for the item.
        # * the search must continue in one of the children.
        # * the item must be added to the contents (same searchkey).
        if item.key < self.contents.key:
            if self.left is None:
                self.left = AdtBinarySearchTree(item)
                self.left.parent = self
                return
            else:
                return self.left._search_tree_insert(item)
        elif item.key > self.contents.key:
            if self.right is None:
                self.right = AdtBinarySearchTree(item)
                self.right.parent = self
                return
            else:
                return self.right._search_tree_insert(item)

        if item.key == self.contents.key:
            self.contents.node_content.append(item.node_content[0])
            return

    def __getitem__(self, key):
        """ Interface to the actual _retrieve() method. This method returns the node, not the subtree.

        :param key: The searchkey of which a node is searched.
        :return: The item with searchkey == 'key'.
        :raise : If key is of incorrect type or missing, an exception is raised.
        """
        if not self.is_empty():
            if not isinstance(key, type(self.contents.key)):
                raise TypeError("Unable to get item: key of incorrect type!")

        (bool, subtree) = self._retrieve(key)
        if not bool:
            raise KeyError("Unable to get item: key is missing!")
        if subtree is None:
            return None
        return subtree.contents.node_content[0]

    def __contains__(self, key):
        """ Interface to the actual _retrieve() method. This method returns a bool.

        :param key: The searchkey of which a node is searched.
        :return: False if there is no node with the searchkey == 'key', True otherwise.
        """
        return self._retrieve(key)[0]

    def _retrieve(self, key):
        """ Retrieves an item with the given searchkey.

        :param key: The searchkey of which a node is searched.
        :return: (False, None) if there is no node with the searchkey == 'key', (True, subtree) otherwise.
        """
        if self.contents is None and (self.parent is None):       # if the whole tree is empty, false is returned
            return (False, None)
        # If here, the key is compared to the key of the content. If they are not equal and the (sub)tree has children/a
        # child, the search will continue in a child.
        if key < self.contents.key and self.left is not None:
            return self.left._retrieve(key)
        elif key > self.contents.key and self.right is not None:
            return self.right._retrieve(key)
        if key == self.contents.key:
            return (True, self)
        else:
            return (False, None)

    def inorder_traversal(self, visit_function):
        """ Visits the tree's keys in inorder traversal.

        :param visit_function: A function that performs a certain action.
        """
        if self.is_empty():
            return
        if self.left:
            self.left.inorder_traversal(visit_function)
        for item in self.contents.node_content:
            visit_function(item)
        if self.right:
            self.right.inorder_traversal(visit_function)


    def _inorder_successor(self, right_child):
        """ Returns the inorder successor. Important: the subtree with which this method is called is always the right
        subtree of the (sub)tree of which we search the inorder successor. This enables the method to search to the most
        left node.

        :param right_child: The right subtree of the node of which the inorder successor is searched.
        :return: The subtree containing the inorder successor.
        """
        # As long as there is a left child, the search will continue. If the tree has no left child, it's content is the
        # inorder successor.
        if right_child.left is not None:
            return self._inorder_successor(right_child.left)
        else:
            return right_child

    def _act_remove(self):
        """ Removes a node in a recursively, which is the reason for it being a seperate function from __delitem__().
        """
        if self._no_children() is True:
            if self.parent:  # Making sure the node is deleted from it's parent's children.
                if self.parent.left == self:
                    self.parent.left = None
                else:
                    self.parent.right = None
            else:   # self is the root
                self.contents = None

        # If there is only one child, transfer the contents and it's children to this (sub)tree.
        if (self.left is None) and self.right:
            self.contents = self.right.contents
            self.left = self.right.left
            self.right = self.right.right
        elif (self.right is None) and self.left:
            self.contents = self.left.contents
            self.right = self.left.right
            self.left = self.left.left
        # If there are two children, swap places with the inorder successor and carry this function out on that subtree.
        elif self.left and self.right:
            inorderSucc = self._inorder_successor(self.right)
            self.contents = inorderSucc.contents
            inorderSucc._act_remove()

        # The possibly moved children of this (sub)tree should know that this is their parent.
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __delitem__(self, key):
        """ Checks whether a node with the given 'key' is present, if so the remove will be carried out.

        :param key: The searchkey of the node to be deleted.
        :raise: If key is of incorrect type or missing, an exception is raised.
        """
        if not self.is_empty():
            if not isinstance(key, type(self.contents.key)):
                raise TypeError("Unable to delete item: key of incorrect type!")

        (bool, subtree) = self._retrieve(key)

        if bool is False:           # There is no node with the given key.
            raise KeyError("Unable to delete item: key is missing!")
        if len(subtree.contents.node_content) > 1:   # If there are multiple items with the given searchkey
            del subtree.contents.node_content[0]
            return
        else:
            return subtree._act_remove()

    def __repr__(self):
        """ The base method for creating a string that represents the dot-code.

        :return: A string containing the dot-code to create a graph.
        :raise: If the tree is empty, an exception is raised.
        """
        string = "digraph bst {\nnode [shape=Mrecord];\n"
        if not self.is_empty():
            string += self._get_string("", 0, 0)[0]
        string += "}"
        return string

    def _get_string(self, string, nr, parentnr):
        """ Makes the .dot string of the whole tree.

        :param : String is the current string that is updated during the method, nr is the current node-nr and parentnr
        is the number of the node of the parent (needed to draw the edges).
        :return: It returns the current string and current number (used as name for
        the node).
        """
        nr += 1
        root_name = "node" + str(nr)
        string += root_name + ' [label="' + str(self.contents.key) + ": " + str(self.contents.node_content) + '"];\n'

        if self.right and self.left:
            (string, newnr) = self.left._get_string(string, nr, nr)
            (string, nr) = self.right._get_string(string, newnr, nr)
        if not self.left and self.right:
            invis = "inv" + str(nr) + "left"
            string += invis + ' [style="invisible"];\n'
            string += root_name + ' -> ' + invis + " [style=invis];\n"
            (string, nr) = self.right._get_string(string, nr, nr)
        if not self.right and self.left:
            (string, nr) = self.left._get_string(string, nr, nr)
            # self.left._get_string(string, nr)
            invis = "inv" + str(nr) + "right"
            string += invis + ' [style="invisible"];\n'
            string += root_name + ' -> ' + invis + " [style=invis];\n"
        if self.parent:
            string += "node" + str(parentnr) + " -> " + root_name + ";\n"
        return string, nr

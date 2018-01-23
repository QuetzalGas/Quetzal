class _TreeItem:
    def __init__(self, key=None, item=None):
        if item is None:
            self.node_content = None
        else:
            self.node_content = [item]
        self.key = key

class AdtTwoThreeTree:
    def __init__(self):
        self.contents = []
        self.children = []
        self.parent = None

    def _no_children(self):
        """ Checks if the tree has children or not.

        :return: True if it doesn't have any children, false otherwise.
        """
        return len(self.children) == 0

    def _node_type(self):
        """ Returns the node_type of the tree's contents. (0-node, 2-node or 3-node)

        :return: A number representing the node_type (0, 2 or 3)
        """
        # If the (sub)tree's content is empty, its type is 0. Otherwise, its type = 1 + amount of nodes.
        lengte = len(self.contents)
        if lengte > 0:
            return lengte + 1
        return lengte

    def is_empty(self):
        """ Checks whether the (sub)tree's content (and therefore children) is empty.

        :return: True if the (sub)tree's content is empty, false otherwise.
        """
        return len(self.contents) == 0

    def _compare_and_put_in_place(self, newItem):
        """ Compares the keys of the (sub)tree's nodes and newItem and puts newItem in the correct position.

        :param newItem: Item to be inserted in the (sub)tree's contents. It is of type TreeItem.
        :return: A value representing the place of the insertion.
        """
        if self.is_empty():   # If the (sub)tree is empty, newItem is inserted in the contents.
            self.contents.append(newItem)
            return 1

        if self._node_type() == 2:                      # If it's a 2-node, comparison of the only key must take place
            if newItem.key < self.contents[0].key:
                self.contents.append(self.contents[0])  # The current only node must make place for newItem by moving
                self.contents[0] = newItem
                return 0
            else:
                self.contents.append(newItem)           # If the key of newItem > self.contents[0].key, appending the
                return 1                                # (sub)tree's contents with newItem will suffice.

        if self._node_type() == 3:                      # If it's a 3-node, comparison of the 1st, and possibly 2nd
            if newItem.key < self.contents[0].key:      # key take place.
                self.contents.insert(0, newItem)
                return 0
            if newItem.key < self.contents[1].key:
                self.contents.insert(1, newItem)
                return 2
            if newItem.key > self.contents[1].key:
                self.contents.append(newItem)
                return 1

    def _split(self):
        """ Splits a node with 4-nodes to two new subtrees and brings the middle element up. If it's an internal node,
        the children are moved.
        """
        wortelScenario = False              # If true, the contents of pNode (see later) must be moved to this tree.

        if self.parent is None:             # If there isn't a parent, a new tree 'pNode' must be made, this will
            pNode = AdtTwoThreeTree()       # enable the splitting in the root-scenario.
            wortelScenario = True
        else:                               # If there is a parent, 'pNode' should be the parent.
            pNode = self.parent             # The parent will have 2 new children (n1 and n2) and should not have this
            pNode.children.remove(self)     # tree as it's child anymore.

        n1 = AdtTwoThreeTree()              # n1 and n2 will contain the left and right TreeItems and the corresponding
        n2 = AdtTwoThreeTree()              # children (if it's an internal node).
        n1._do_insert(self.contents[0])
        n2._do_insert(self.contents[2])
        n1.parent = pNode                   # Be sure to have pNode as n1's and n2's parent.
        n2.parent = pNode

        # If we are dealing with an internal node: the two left children are moved to n1, the two right children to n2.
        if not self._no_children():
            n1.children.append(self.children[0])
            n1.children.append(self.children[1])

            n2.children.append(self.children[2])
            n2.children.append(self.children[3])

            # There must be made sure that the children know who their new parent is.
            n1._set_children_parent()
            n2._set_children_parent()

        # The middle TreeItem will be moved to and inserted in pNode, result represents the place of the insertion.
        result = pNode._compare_and_put_in_place(self.contents[1])

        if result == 0:     # If true, this tree was a left child, insert n1 & n2, to get them as first children.
            pNode.children.insert(0, n1)
            pNode.children.insert(1, n2)
        if result == 1:     # If true, this tree was a right child, append n1 & n2, to get them as right children.
            pNode.children.append(n1)
            pNode.children.append(n2)
        if result == 2:     # If true, this tree was the middle child, so n1 & n2 should be inserted at index 1 & 2.
            pNode.children.insert(1, n1)
            pNode.children.insert(2, n2)

        if wortelScenario:
            # Since removing the very base of the tree is not possible, one must take over the contents of pNode:
            self.contents = pNode.contents
            self.children = pNode.children
            self._set_children_parent()     # Still making sure that all children know that this tree is their parent.

        # If now pNode is a 4-node, the split algorithm must be applied on it.
        if not wortelScenario and pNode._node_type() == 4:
            pNode._split()

    def __setitem__(self, key, item):
        """ Inserts a node with the given 'key' as searchkey and 'item' as content.

        :param key:  The searchkey of the new node.
        :param item: The content of the new node.
        :raise: If key and/or item are of incorrect type, an exception is raised.
        """
        if not self.is_empty():
            if not isinstance(key, type(self.contents[0].key)) or not isinstance(item, type(self.contents[0].node_content[0])):
                raise TypeError("Unable to insert: key and/or item of incorrect type!")
        self._do_insert(_TreeItem(key, item))

    def _do_insert(self, newItem):
        """ Adds a newItem to the tree. Multiple items with the same searchkey are allowed.

        :param newItem: A node of type _TreeItem.
        """
        if self._node_type() == 0:              # When the very root of the whole tree is empty.
            self.contents.append(newItem)
            return

        if self.contents[0].key == newItem.key:     # Checking if newItem's key == left-TreeItems's key
            self.contents[0].node_content.append(newItem.node_content[0])
            return
        if self._node_type() == 3:
            if self.contents[1].key == newItem.key:
                self.contents[1].node_content.append(newItem.node_content[0])
                return
            if self._no_children():
                self._compare_and_put_in_place(newItem)     # Put newItem in it's correct place, the
                # root will now contains too many nodes, so the split algorithm is called.
                return self._split()
            else:   # If the (sub)tree does have children, the search must continue in the correct one.
                if newItem.key < self.contents[0].key:
                    return self.children[0]._do_insert(newItem)
                elif newItem.key < self.contents[1].key:
                    return self.children[1]._do_insert(newItem)
                else:
                    return self.children[2]._do_insert(newItem)
        if self._node_type() == 2:
            if self._no_children():
                self._compare_and_put_in_place(newItem)
                return
            elif self.contents[0].key > newItem.key:
                return self.children[0]._do_insert(newItem)
            else:
                return self.children[1]._do_insert(newItem)

    def _inorder_successor(self):
        """ Returns the inorder successor. The subtree of which this method is called is always the right subtree of
        the (sub)tree of which we search the inorder successor. It enables the method to search for the most left node.

        :return: The tree containing the inorder successor.
        """
        # Key principle: Once right, tons left.
        if self._no_children():
            return self
        else:
            return self.children[0]._inorder_successor()

    def __getitem__(self, key):
        """ Searches for the given 'key' inside the whole tree.

        :param key: The searchkey of which a node is searched.
        :return: The item with searchkey == 'key'.
        :raise: If the given 'key' is of incorrect type or missing, an exception is raised.
        """
        if not isinstance(key, type(self.contents[0].key)):
            raise TypeError("Unable to get item: key of incorrect type!")

        (boolean, subtree, index) = self._retrieve(key)
        if not boolean:
            raise KeyError("Unable to get item: key is missing!")
        if subtree is None:
            return None
        return subtree.contents[index].node_content[0]  # return the first item in node

    def _retrieve(self, key):
        """ Searches for the given 'key' inside the whole tree.

        :param key: The searchkey of which a node is searched.
        :return: (False, None, 0) if there is no node with the searchkey == 'key', (True, node, index) otherwise.
        """
        if self.is_empty():
            return False, None, 0

        current = self
        while current is not None:
            counter = 0
            # Looping over the (sub)tree's contents to check if there is a TreeItem's searchkey equal to the given key.
            for nodes in current.contents:
                if nodes.key == key:
                    return True, current, counter
                counter += 1
            # If it's not found, then there must be checked if we can look any further in the subtrees or not.
            if current._no_children():
                return False, None, 0
            if key < current.contents[0].key:
                current = current.children[0]
                continue
            if len(current.contents) == 2 and key > current.contents[1].key:
                current = current.children[2]
                continue
            else:
                current = current.children[1]


    def __contains__(self, key):
        """ Does the action of the _retrieve(key), but only returns a boolean.

        :param key: The searchkey of which a node is searched.
        :return: True if there is a node with searchkey == 'key', false otherwise.
        """
        return self._retrieve(key)[0]

    def _fix(self):
        """ Executes the fix algorithm, which means merging the a parent's TreeItem with the 2-node neighbour
        OR moving the a parent's TreeItem to this tree and a neighbour's TreeItem to the parent's node.
        """
        """ note: When it says 'this tree', the 'self' is meant. It can be a subtree.
        note2: Always keep in mind that an internal tree that calls this algorithm has but one child."""
        # When dealing with the root, it must take everything of it's (one and only) child.
        if self.parent is None:
            self.contents = self.children[0].contents
            self.children = self.children[0].children
            self._set_children_parent()
            return  # There need not be more fixing.

        index = self.parent.children.index(self)    # Searching the index of this subtree in its parent's children
        # index_parent : the index in the parent's contents at the corresponding side of this subtree
        # index_buur : the index of the neighbour in the parent's children's list
        # delBuurItemOrMerge : the index to delete the neighbour's TreeItem or the index to merge the parent's TreeItem
        # insOwnItemOrChild : the index to insert in this tree an TreeItem (from parent) or child (from neighbour)
        if index == 0:
            (index_parent, index_buur, delBuurItemOrMerge, insOwnItemOrChild) = (0, 1, 0, 1)
        elif index == 1:
            (index_parent, index_buur, delBuurItemOrMerge, insOwnItemOrChild) = (0, 0, 1, 0)
        else:
            (index_parent, index_buur, delBuurItemOrMerge, insOwnItemOrChild) = (1, 1, 1, 0)

        # If the neighbour is a 3-node, then the parent's root (at the side of this tree) will be set as this tree's
        # root. One node of the neighbour will replace the parent's moved root.
        if self.parent.children[index_buur]._node_type() == 3:
            self.contents.append(self.parent.contents[index_parent])
            self.parent.contents[index_parent] = self.parent.children[index_buur].contents[delBuurItemOrMerge]
            del self.parent.children[index_buur].contents[delBuurItemOrMerge]
            # If's an internal node, then the child of the neighbour at the correct side has to move to this tree.
            if not self._no_children():
                # => (2*delBuurItemOrMerge) -> 0 if it's a left child: to take most left child of neighbour
                #                           -> 2 if it's a right or middle child: to take most right child of neighbour
                self.children.insert(insOwnItemOrChild, self.parent.children[index_buur].children[2*delBuurItemOrMerge])
                del self.parent.children[index_buur].children[2*delBuurItemOrMerge]
                self._set_children_parent()

        # If the neighbour is a 2-node, merge a/the parent's root node with the neighbour's root. If this tree has a
        # child, it needs to move to the neighbour.
        else:
            self.parent.children[index_buur].contents.insert(delBuurItemOrMerge, self.parent.contents[index_parent])
            if not self._no_children():
            # neighbour has 2 children already, new child's index is: 0 (left) or 2 (right). Never at index 1 (middle).
                self.parent.children[index_buur].children.insert(2*delBuurItemOrMerge, self.children[0])
                self.parent.children[index_buur]._set_children_parent()

            del self.parent.contents[index_parent]
            del self.parent.children[index]     # This subtree must be removed, so delete it as a child from the parent.

        if self.parent._node_type() == 0:       # If the parent is empty now, the fix algorithm must be called again.
            self.parent._fix()


    def __delitem__(self, key):
        """ Searches for the node with searchkey == 'key'. If present, this node is deleted.

        :param key: The searchkey of the node to be deleted. Key should be of the same type as the tree's searchkeys.
        :raise: If the given 'key' is of incorrect type or missing, an exception is raised.
        """
        if self.is_empty():
            raise KeyError("Unable to delete item: key is missing!")

        if not isinstance(key, type(self.contents[0].key)):
            raise TypeError("Unable to delete item: key of incorrect type!")

        (boolean, current, counter) = self._retrieve(key)
        if not boolean:
            raise KeyError("Unable to delete item: key is missing!")

        # If there are multiple items with the same searchkey, removing only one of those will suffice.
        if len(current.contents[counter].node_content) > 1:
            del current.contents[counter].node_content[0]   # deleting first item in node_content
            return

        if current._no_children():
            # The node with the given key will have to be deleted.
            del current.contents[counter]
            if current.parent is not None:
                # If the (sub)tree is an empty leaf, the fix-algorithm will be called.
                if current.is_empty():
                    current._fix()

        # If we're dealing with an internal node, then it must swap positions with it's inorder successor.
        else:
            inord_succ = current.children[counter+1]._inorder_successor()
            # The inorder successor is in the left TreeItem, always, that is the whole essence of the inorder successor.
            current.contents[counter] = inord_succ.contents[0]
            del inord_succ.contents[0]
            if inord_succ.is_empty():     # If the inorder successor's node is empty after deleting, the fix algorithm
                inord_succ._fix()         # must be called.
            return


    def _set_children_parent(self):
        """ Sets the parent of the (sub)tree's children to this node.
        """
        for child in self.children:
            child.parent = self

    def inorder_traversal(self, visit_function):
        """ Visits the tree's keys in inorder traversal.

        :param visit_function: A function that performs a certain action.
        """
        if self.is_empty():
            return
        if self._no_children():
            for node in self.contents:
                for item in node.node_content:
                    visit_function(item)
        else:
            for i in range(len(self.children)):
                self.children[i].inorder_traversal(visit_function)
                if i < self._node_type() - 1: # visit parent's node with same index as child, but not after last child
                    for item in self.contents[i].node_content:
                        visit_function(item)

    def __repr__(self):
        """ The base method for creating a string that represents the dot-code.

        :return: A string containing the dot-code to create a graph.
        :raise: If the tree is empty, an exception is raised.
        """
        string = "digraph 23 {"
        if not self.is_empty():
            string += "\nnode [shape=Mrecord];"
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
        left_node_string = str(self.contents[0].key) + ": " + str(self.contents[0].node_content)
        if self._node_type() == 3:
            right_node_string = str(self.contents[1].key) + ": " + str(self.contents[1].node_content)

        nodeName = "node" + str(nr)   # used as the name of the node itself, not the visual label.

        string += "\n" + nodeName + ' [label=" ' + left_node_string + '"];'
        if self._node_type() == 3:
            string += "\n" + nodeName + ' [label=" ' + left_node_string + '| ' + right_node_string + '"];'

        if not self._no_children():     # If the (sub)tree has children, the same algorithm must be applied on them.
            if self._node_type() == 2:
                (string, newnr) = self.children[0]._get_string(string, nr, nr)
                (string, nr) = self.children[1]._get_string(string, newnr, nr)

            elif self._node_type() == 3:
                (string, newnr) = self.children[0]._get_string(string, nr, nr)
                (string, newnr) = self.children[1]._get_string(string, newnr, nr)
                (string, nr) = self.children[2]._get_string(string, newnr, nr)

        if self.parent is not None:     # The parents nodename is given by it's leftItem's key, so an edge can be added.
            nameParent = "node" + str(parentnr)
            string += "\n" + nameParent + " -> " + nodeName + ";"   # adding the edge between parent and this subtree.
        return string, nr

    """
    Webpages I used to get information about the dot-language.
    - Node Shapes, geraadpleegd op 5/12/2017 via http://www.graphviz.org/doc/info/shapes.html
    - Node, Edge and Grapgh Attributes. Geraadpleegd op 5/12/2017 via http://www.graphviz.org/doc/info/attrs.html
    """

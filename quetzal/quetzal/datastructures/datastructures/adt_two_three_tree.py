class _TreeItem:
    def __init__(self, item=None, key=None, next=None):
        self.item = item
        self.key = key
        self.next = next

class AdtTwoThreeTree:
    def __init__(self):
        self.root = []
        self.children = []
        self.parent = None

    def _no_children(self):
        """ Checks if the tree has children or not.

        :return: True if it doesn't have any children, false otherwise.
        """
        return len(self.children) == 0

    def _node_type(self):
        """ Returns the node_type of the tree's root. (2-node, 3-node or 0-node)

        :return: A number representing the node_type (0, 2 or 3)
        """
        # If the root is empty, I consider it's type to be 0. When it isn't empty, the node_type = 1 + amount of nodes.
        lengte = len(self.root)
        if lengte > 0:
            return lengte + 1
        return lengte

    def is_empty(self):
        """ Checks whether the tree's root (and therefore children) is empty.

        :return: True if the root is empty, false otherwise.
        """
        return len(self.root) == 0

    def _compare_and_put_in_place(self, newItem):
        """ Compares newItem with the key's of the root-nodes and puts it in the correct position.

        :param newItem: Item to be inserted in the root.
        :return: A value representing the place of the insertion. This value is used inside the _split() method.
        """
        if self.is_empty():                       # If the root is empty, newItem is inserted in the rootlist
            self.root.append(newItem)
            return 1

        if self._node_type() == 2:                      # If it's a 2-node, comparison of the only key must take place
            if newItem.key < self.root[0].key:
                self.root.append(self.root[0])          # The current only node must make place for newItem by moving
                self.root[0] = newItem
                return 0
            else:
                self.root.append(newItem)               # If the key of newItem > self.root[0].key, append the root with
                return 1                                # newItem will suffice. (no need to move the node in the root)

        if self._node_type() == 3:                      # If it's a 3-node, comparison of the 1st, and possibly 2nd
            if newItem.key < self.root[0].key:          # key take place.
                self.root.insert(0, newItem)
                return 0
            if newItem.key < self.root[1].key:
                self.root.insert(1, newItem)
                return 2
            if newItem.key > self.root[1].key:
                self.root.append(newItem)
                return 1

    def _split(self):
        """ Splits a node with 3 root-nodes to two new subtrees and brings the middle root-node up. If it's an internal
        node the children are moved.
        """
        wortelScenario = False              # If true, the contents of pNode (see later) must be moved to this tree.

        if self.parent is None:             # If there isn't a parent, a new tree 'pNode' must be made, this will
            pNode = AdtTwoThreeTree()       # enable the splitting in the root-scenario.
            wortelScenario = True
        else:                               # If there is a parent, 'pNode' should be the parent.
            pNode = self.parent             # The parent will have 2 new children (n1 and n2) and should not have this
            pNode.children.remove(self)     # tree as it's child anymore

        n1 = AdtTwoThreeTree()              # n1 and n2 will contain the left and right roots and the corresponding
        n2 = AdtTwoThreeTree()              # children (if it's an internal node).
        n1._do_insert(self.root[0])
        n2._do_insert(self.root[2])
        n1.parent = pNode                   # Be sure to have pNode as n1's and n2's parent.
        n2.parent = pNode

        # If we are dealing with an internal node: the two left children are moved to n1, the two right children to n2.
        if not self._no_children():
            n1.children.append(self.children[0])
            n1.children.append(self.children[1])

            n2.children.append(self.children[2])
            n2.children.append(self.children[3])

            # There must be made sure that the children know who their new parent is. Otherwise, problems will occur.
            n1._set_children_parent()
            n2._set_children_parent()

        # The middle root will be moved to pNode, result represents the place of the middle root inside the pNode
        result = pNode._compare_and_put_in_place(self.root[1])

        if result == 0:     # If true, this tree was a left child, insert n1 & n2, to get them as first children
            pNode.children.insert(0, n1)
            pNode.children.insert(1, n2)
        if result == 1:     # If true, this tree was a right child, append n1 & n2, to get them as the last children
            pNode.children.append(n1)
            pNode.children.append(n2)
        if result == 2:     # If true, this tree was the middle child, so n1 & n2 should be insert at index 1 & 2
            pNode.children.insert(1, n1)
            pNode.children.insert(2, n2)

        # Since removing the very base of the tree is not possible, one must take over the contents of pNode:
        if wortelScenario:
            self.root = pNode.root
            self.children = pNode.children
            self._set_children_parent()     # Still making sure that all children know that this tree is their parent.

        # If now pNode has more then two items in it's root, the split algorithm must be applied on it.
        if not wortelScenario and pNode._node_type() == 4:
            pNode._split()

    def __setitem__(self, key, item):
        """ Inserts a node with the given 'key' as searchkey and 'item' as content.

        :param key:  The searchkey of the new node.
        :param item: The content of the new node.
        :raise: If key or item are of incorrect type, an exception is raised.
        """
        if not self.is_empty():
            if not isinstance(key, type(self.root[0].key)) or not isinstance(item, type(self.root[0].item)):
                raise TypeError("Unable to insert: key and/or item of incorrect type!")
        self._do_insert(_TreeItem(item, key))

    def _do_insert(self, newItem):
        """ Adds a newItem to the tree. Multiple items with the same searchkey are allowed.

        :param newItem: A node of type _TreeItem.
        """
        if self._node_type() == 0:              # When the very root of the whole tree is empty.
            self.root.append(newItem)
            return

        if self.root[0].key == newItem.key:     # Checking if newItem's key == leftroots's key
            newItem.next = self.root[0]         # If so, the linked list principle is followed. NewItem's added to the
            self.root[0] = newItem              # chain of Nodes.
            return
        if self._node_type() == 3:
            if newItem.key == self.root[1].key:
                newItem.next = self.root[1]
                self.root[1] = newItem
                return
            if self._no_children():
                self._compare_and_put_in_place(newItem)     # Put newItem in it's correct place, the root will now
                # contains to many nodes (linked list of nodes), so the split algorithm should be called.
                return self._split()
            else:   # If the (sub)tree does have children, the search must continue in the correct one.
                if newItem.key < self.root[0].key:
                    return self.children[0]._do_insert(newItem)
                elif newItem.key < self.root[1].key:
                    return self.children[1]._do_insert(newItem)
                else:
                    return self.children[2]._do_insert(newItem)
        if self._node_type() == 2:
            if self._no_children():
                self._compare_and_put_in_place(newItem)
                return
            elif self.root[0].key > newItem.key:
                # zoek dan verder in het rechterkind.
                return self.children[0]._do_insert(newItem)
            else:
                return self.children[1]._do_insert(newItem)

    def _inorder_successor(self):
        """ Returns the inorder successor. The subtree with which this method is called is always the right subtree of
        the (sub)tree of which we search the inorder successor. It enables the method to search for the most left node.

        :return: The tree of type AdtTwoThreeTree that is the inorder successor.
        """
        # Key principle: Once right, tons left. (An inorder successor is at the most left node of the right subtree.)
        if self._no_children():
            return self
        else:
            return self.children[0]._inorder_successor()

    def __getitem__(self, key):
        """ Searches for the given 'key' inside the whole tree.

        :param key: The searchkey of which a node is searched.
        :return: (False, None) if there is no node with the searchkey == 'key', (True, node) otherwise.
        :raise: If the given 'key' is of incorrect type or the tree is empty, an exception is raised.
        """
        if self.is_empty():
            return False, None

        if not isinstance(key, type(self.root[0].key)):
            raise TypeError("Unable to get item: key of incorrect type!")

        current = self
        while next is not None:
            counter = 0
            # Looping over the root-nodes to check if any of them have a searchkey equal to the given key.
            for nodes in current.root:
                if nodes.key == key:
                    return True, current.root[counter]
            # If it's not found, then there must be checked if we can look any further in the subtrees or not.
            if current._no_children():
                return False, None
            if key < current.root[0].key:
                current = current.children[0]
                continue
            if len(current.root) == 2 and key > current.root[1].key:
                current = current.children[2]
                continue
            else:
                current = current.children[1]

    def __contains__(self, key):
        """ Does the action of the __getitem__(key), but only return a boolean.

        :param key: The searchkey of which a node is searched.
        :return: True if there is a node with searchkey == 'key', false otherwise.
        """
        return self.__getitem__(key)[0]

    def _fix(self):
        """ Excecutes the fix algorithm, which means merging the (correct) parent's root-node with the 2-node neighbour
        OR moving the (correct) parent's root-node to this tree and a neighbour's root-node to the parent's root.
        """
        # If we're dealing with the root here, then it must take everything of it's (one and only) child.
        if self.parent is None:
            self.root = self.children[0].root
            self.children = self.children[0].children
            self._set_children_parent()
            return  # There need not be more fixing.

        # In these following few lines, indexes used to move nodes and subtree's are fetched.
        # Verschil is used at several places to get the right index_root (index in the parent's root, depending on the
        # position of this tree (left, mid, right child))
        verschil = -1
        index = self.parent.children.index(self)
        if index == 0:
            verschil = 1
        index_buur = ( index - 1 )%2    # the index representing the neighbour's place (left, mid, right child)
        index_root = index + min(0, verschil)   # the index of the root of the parent should be one if it's a left child,
        # mid child or 'right child of 2-node parent', only when it's a right child of a 3-node parent: index_root = 1

        # If the neighbour is a 3-node, then the parent's root (at the side of the tree) will be set as this tree's
        # root. One node of the neighbour will replace the parent's moved root.
        if self.parent.children[index_buur]._node_type() == 3:
            self.root.append(self.parent.root[index_root])
            self.parent.root[index_root] = self.parent.children[index_buur].root[min(index, 1)]
            del self.parent.children[index_buur].root[min(index, 1)]
            # If's an internal node, then the child of the neighbour at the correct side has to move to the tree.
            if not self._no_children():
                # this tree = right or mid child: move [neighbour-child at index 2 (|-1-1|=2)] to [own child: index 0]
                # this tree = left child: move [neighbour-child at index 0 (|-1+1|=0)] to [own child:  index 1]
                index_child_buur = abs(-1+verschil)     # neighbour-child index
                index_child_self = min(verschil+1, 1)   # own child index
                self.children.insert(index_child_self, self.parent.children[index_buur].children[index_child_buur])
                del self.parent.children[index_buur].children[index_child_buur]
                self._set_children_parent()

        # If the neighbour is a 2-node, merge a/the parent's root node with the neighbour's root
        else:
            index_insert_parent_root = (index + index_root)%2   # index in neighbour's root to merge parent's node
            # --> index needs to be 1 if this tree's not a left child ==> [(1+0)%2 = 1] or [(2+1)%2 = 1]
            # --> index needs to be 0 if this tree's a left child ==> [(0+0)%2 = 0]
            self.parent.children[index_buur].root.insert(index_insert_parent_root, self.parent.root[index_root])

            if not self._no_children():
                self.parent.children[index_buur].children.insert(2*index_insert_parent_root, self.children[0])
                self.parent.children[index_buur]._set_children_parent()

            del self.parent.root[index_root]
            del self.parent.children[index]     # This subtree must be removed, so delete it as a child from the parent.

        if self.parent._node_type() == 0:       # The parent may not be empty, so the fix algorithm should be called.
            self.parent._fix()


    def __delitem__(self, key):
        """ Searches for the node with searchkey == 'key'. If present, this node is deleted.

        :param key: The searchkey of the node to be deleted. Key should be of the same type as the tree's searchkeys.
        :return: True if there was a node with 'key' as searchkey, this node is deleted. False otherwise.
        :raise: If the given 'key' is of incorrect type, an exception is raised.
        """
        # If the table is empty, then the key will surely not be present.
        if self.is_empty():
            return False

        if not isinstance(key, type(self.root[0].key)):
            raise TypeError("Unable to delete item: key of incorrect type!")

        # In the following piece of code, the (sub)tree of the key is searched and also it's position in the root
        current = self
        counter = 0         # will present the key's position
        found = 0
        while next is not None:
            counter = 0
            # Looping over the root-nodes to check if any of them have a searchkey equal to the given key.
            for counter in range(len(current.root)):
                if current.root[counter].key == key:
                    found = 1
                    break
            # If it's found, then hooray we can break out of this while-loop and continue the adventure.
            if found:
                break
            # If it's not found, then there must be checked if we can look any further in the subtrees or not.
            if current._no_children():
                return False
            if key < current.root[0].key:
                current = current.children[0]
                continue
            if len(current.root) == 2 and key > current.root[1].key:
                current = current.children[2]
                continue
            else:
                current = current.children[1]

        # If there are multiple nodes with the same searchkey, removing only one of those nodes will suffice.
        if current.root[counter].next is not None:
            current.root[counter] = current.root[counter].next
            return True

        # Only item in tree, so just set the root to an emty list
        if current.is_empty():
            self.root = []
            return True

        if current._no_children():
            # The node with the given key will have to be deleted, when here.
            del current.root[counter]
            # If the (sub)tree is an empty leaf, the _fix-algrorithm will be called.
            if current.is_empty():
                current._fix()

        # If we're dealing with an internal node, then it must swap positions with it's inorder successor.
        else:
            inordSuc = current.children[counter+1]._inorder_successor()
            # Using a copy not to lose the inorder successor. The inorder successor is at the left root, always,
            # that is the whole essence of the inorder successor.
            kopie = inordSuc.root[0]
            inordSuc.root[0] = current.root[counter]
            current.root[counter] = kopie
            return inordSuc.__delitem__(key)


    def _set_children_parent(self):
        """ Sets the parent of the (sub)tree's children to this node.
        """
        for child in self.children:
            child.parent = self

    def __repr__(self):
        """ The base method for creating a string that represents the dot-code.
        :return: A string containing the dot-code to create a graph.
        :raise: If the tree is empty, an exception is raised.
        """
        if self.is_empty():
            raise KeyError("Unable to create a dot-string of an empty tree.")
        string = "digraph 23 {\nnode [shape=Mrecord];\n"\
            + 'node [shape=Mrecord, style=filled, fillcolor="#34373d", fontcolor="#1aba4a",'\
            + ' fontname=Ubuntu, compound=true, color="#1aba4a"];\n'\
            + 'edge [color="#1aba4a"];\n'\
            + 'graph [rankdir=TD, bgcolor="#34373d"];'
        string += self._get_string()
        string += "}"
        return string

    def _get_node_label(self, node):
        """ Adds all node-items with the same searchkey to a string.

        :return: A string representing the labels of the nodes with the same searchkey. The are divided by comma's.
        """
        string = ""
        while node is not None:
            string += node.item
            if node.next is not None:
                string += ", "
            node = node.next
        return string

    def _get_string(self):
        """ Makes the .dot string of the whole tree. It returns the current string, which is used not only outside this
        method. Inside this method each string of the children is added to the current one, if this tree has children.

        :return: A string containing all information of the nodes and the edges.
        """
        left_node_string = self._get_node_label(self.root[0])
        if self._node_type() == 3:
            right_node_string = self._get_node_label(self.root[1])

        nodeName = "node" + str(self.root[0].key)   # used as the name of the node itself, not the visual label.

        string = "\n" + nodeName + ' [label=" ' + left_node_string + '"];'
        if self._node_type() == 3:
            string += "\n" + nodeName + ' [label=" ' + left_node_string + '| ' + right_node_string + '"];'

        if not self._no_children():     # If the (sub)tree has children, the same algorithm must be applied on them.
            if self._node_type() == 2:
                string += self.children[0]._get_string()
                string += self.children[1]._get_string()

            elif self._node_type() == 3:
                string += self.children[0]._get_string()
                string += self.children[1]._get_string()
                string += self.children[2]._get_string()

        if self.parent is not None:     # The parents nodename is given by it's leftroot key, so an edge can be added.
            nameParent = "node" + str(self.parent.root[0].key)
            string += "\n" + nameParent + " -> " + nodeName + ";"   # adding the edge between parent and this subtree.
        return string

    """
    Webpagina's die ik heb geraadpleegd om de .DOT file te maken.
    - Node Shapes, geraadpleegd op 5/12/2017 via http://www.graphviz.org/doc/info/shapes.html
    - Node, Edge and Grapgh Attributes. Geraadpleegd op 5/12/2017 via http://www.graphviz.org/doc/info/attrs.html
    """
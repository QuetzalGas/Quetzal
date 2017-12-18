class TreeNode:
    def __init__(self):
        self.items = [None] * 3
        self.parent = None
        self.children = [None] * 4
        self.amount = 0

    def isLeaf(self):
        for link in self.children:
            if link is not None:
                return False
        return True

    def getMaxSearchKey(self):
        max = None
        for item in self.items:
            if item is not None:
                max = item.searchKey
        return max

    def insertItem(self, newItem):
        if newItem is None:
            return False
        for item in self.items:
            if item is not None:
                if item.searchKey == newItem.searchKey:
                    return False
        if self.amount == 0:
            self.items[0] = newItem
        elif self.amount == 1:
            if newItem.searchKey < self.items[0].searchKey:
                self.items[1] = self.items[0]
                self.items[0] = newItem
            else:
                self.items[1] = newItem
        elif self.amount == 2:
            if newItem.searchKey < self.items[0].searchKey:
                self.items[2] = self.items[1]
                self.items[1] = self.items[0]
                self.items[0] = newItem
            elif newItem.searchKey > self.items[1].searchKey:
                self.items[2] = newItem
            else:
                self.items[2] = self.items[1]
                self.items[1] = newItem
        else:
            return False
        self.amount += 1
        return True

    def insertChild(self, newChild):
        if newChild is None:
            return False
        if self.children[0] is None:
            self.children[0] = newChild
        elif self.children[1] is None:
            if newChild.getMaxSearchKey() < self.children[0].getMaxSearchKey():
                self.children[1] = self.children[0]
                self.children[0] = newChild
            else:
                self.children[1] = newChild
        elif self.children[2] is None:
            if newChild.getMaxSearchKey() < self.children[0].getMaxSearchKey():
                self.children[2] = self.children[1]
                self.children[1] = self.children[0]
                self.children[0] = newChild
            elif newChild.getMaxSearchKey() < self.children[1].getMaxSearchKey():
                self.children[2] = self.children[1]
                self.children[1] = newChild
            else:
                self.children[2] = newChild
        elif self.children[3] is None:
            if newChild.getMaxSearchKey() < self.children[0].getMaxSearchKey():
                self.children[3] = self.children[2]
                self.children[2] = self.children[1]
                self.children[1] = self.children[0]
                self.children[0] = newChild
            elif newChild.getMaxSearchKey() < self.children[1].getMaxSearchKey():
                self.children[3] = self.children[2]
                self.children[2] = self.children[1]
                self.children[1] = newChild
            elif newChild.getMaxSearchKey() < self.children[2].getMaxSearchKey():
                self.children[3] = self.children[2]
                self.children[2] = newChild
            else:
                self.children[3] = newChild
        else:
            return False
        return True

    def deleteItem(self, toDelete):
        if toDelete is None or toDelete not in self.items:
            return None, False
        k = 0
        for item in self.items:
            k += 1
            if item == toDelete:
                for i in range(self.amount-k):
                    self.items[k-1] = self.items[k]
                    k += 1
                self.items[self.amount-1] = None
                self.amount -= 1
                return toDelete, True

    def deleteChild(self, toDelete):
        if toDelete is None or toDelete not in self.children:
            return None, False
        k = 0
        for child in self.children:
            k += 1
            if child == toDelete:
                for i in range(self.amount + 1 - k):
                    self.children[k - 1] = self.children[k]
                    k += 1
                self.children[self.amount] = None
                return toDelete, True

    def getSiblings(self):
        if self.parent is None:
            return 0, None
        if self.parent.amount == 1:
            if self.parent.children[0] is self:
                return 1, self.parent.children[1]
            else:
                return 1, self.parent.children[0]
        else:
            if self.parent.children[0] is self:
                return 1, self.parent.children[1]
            elif self.parent.children[1] is self:
                return 2, self.parent.children[0], self.parent.children[2]
            elif self.parent.children[2] is self:
                if self.parent.amount == 2:
                    return 1, self.parent.children[1]
                else:
                    return 2, self.parent.children[1], self.parent.children[3]
            else:
                return 1,self.parent.children[2]

    def allSiblings1Nodes(self):
        if self.getSiblings()[0] == 0:
            return False
        elif self.getSiblings()[0] == 1:
            if self.getSiblings()[1].amount == 1:
                return True
            else:
                return False
        else:
            if self.getSiblings()[1].amount == 1 and self.getSiblings()[2].amount == 1:
                return True
            else:
                return False

    def whichChild(self):
        if self.parent is None:
            return None
        for i in range(4):
            if self.parent.children[i] is self:
                return i

    def print(self):
        for item in self.items:
            if item is None:
                continue
            else:
                print(item.item, end=" ")
        print()
        if not self.isLeaf():
            for child in self.children:
                if child is not None:
                    child.print()

class TreeItem:
    def __init__(self, key, item):
        self.searchKey = key
        self.item = item

class AdtTwoThreeFourTree:
    """
    TableItemType is het type van de elementen die in de 2-3-4 boom worden opgeslagen.
    Een element heeft een searchKey van het type KeyType.
    """
    def __init__(self):
        """
        Creates an empty 2-3-4 tree.
        Pre: none.
        Post: an empty tree has been created.
        """
        self.root = None

    def __del__(self):
        """
        Deletes a 2-3-4 tree.
        Pre: none.
        Post: the tree is empty.
        """
        self.root = None

    def tableIsEmpty(self):
        """
        Determines if the 2-3-4 tree is empty.
        Pre: none.
        Post: returns True if tree is empty.
        :return: True if empty, False if not.
        """
        return self.root is None

    def splitNode(self, node):
        """
        Splits given node if the node is full (3 items). Transfers one item to parent and creates another sibling. If node is root, a new root is created.
        :param node: Node that needs to be slpit.
        :return: True if node was split, False if not.
        """
        if node.amount != 3:
            return False
        if node.parent is None:
            newRoot = TreeNode()
            newRoot.insertItem(node.items[1])
            node.parent = newRoot
            newRoot.insertChild(node)
            self.root = newRoot
        else:
            node.parent.insertItem(node.items[1])
        newNode = TreeNode()
        newNode.insertItem(node.items[2])
        newNode.parent = node.parent
        if not node.isLeaf():
            node.children[2].parent = newNode
            node.children[3].parent = newNode
            newNode.insertChild(node.children[2])
            newNode.insertChild(node.children[3])
            node.children[2] = None
            node.children[3] = None
        node.parent.insertChild(newNode)
        node.items[2] = None
        node.items[1] = None
        node.amount -= 2
        return True

    def tableInsert(self, key, item):
        """
        Inserts 'newItem' in the 2-3-4 tree
        with items with different searchKeys than the searchKey of 'newItem'.
        Pre: 'newItem' is of type TableItemType
        Post: tree is a valid 2-3-4 tree and returns True if insertion worked.
        :param newItem: item to be added in the tree.
        :return: True if insert worked, False if not.
        """
        newItem = TreeItem(key, item)
        if self.root is None:
            self.root = TreeNode()
            self.root.insertItem(newItem)
        else:
            self.insert(self.root, newItem)

    def insert(self, node, newTreeItem):
        """
        Searches the right leaf to insert newTreeItem, and inserts it immediately.
        :param node: starting point to insert
        :param newTreeItem: item to be inserted
        """
        if node.amount == 3:
            self.splitNode(node)
            current = node.parent   # splitNode reorganised the tree, so current has to be reset to the parent
        else:
            current = node
        if current.isLeaf():
            current.insertItem(newTreeItem)
        else:
            if newTreeItem.searchKey < current.items[0].searchKey:
                self.insert(current.children[0], newTreeItem)
            elif current.items[1] is not None:
                if newTreeItem.searchKey < current.items[1].searchKey:
                    self.insert(current.children[1], newTreeItem)
                elif current.items[2] is not None:
                    if newTreeItem.searchKey < current.items[2].searchKey:
                        self.insert(current.children[2], newTreeItem)
                    else:
                        self.insert(current.children[3], newTreeItem)
                else:
                    self.insert(current.children[2], newTreeItem)
            else:
                self.insert(current.children[1], newTreeItem)

    def inorderTraverseTable(self, visit):
        """
        Traverses the complete 2-3-4 tree in inorder, and calls function visit for each item.
        Pre: 'visit' is a function.
        Post: visit was called for every item in inorder.
        :param visit: function to be called for every item
        """
        self.inorder(self.root, visit)

    def inorder(self, node, visit):
        """
        Traverses 2-3-4 tree in inorder, starting at node, and calls function visit for each item.
        Pre: 'visit' is a function.
        Post: visit was called for every item in inorder.
        :param visit: function to be called for every item
        :param node: starting point for traversal.
        :return: False if node is empty, True if not.
        """
        if node is None:
            return False
        self.inorder(node.children[0], visit)
        visit(node.items[0].item)
        self.inorder(node.children[1], visit)
        if node.items[1] is not None:
            visit(node.items[1].item)
            self.inorder(node.children[2], visit)
            if node.items[2] is not None:
                visit(node.items[2].item)
                self.inorder(node.children[3], visit)
        return True

    def dot(self, node, rootnr, filetext):
        """
        Creates the body of a dot file for the 2-3-4 tree, in the form of a string, starting at node.
        Pre: 'rootnr' is an integer different from 0, 'filetext' is a string, 'node' is a part of the tree
        Post: representation of every node at a level lower than 'node' has been added to the string
        :param node: starting point
        :param rootnr: number to identify starting point 'node'
        :param filetext: string
        :return: adjusted string filetext
        """
        if node is None:
            return filetext
        filetext += "\n\"node"
        filetext += str(rootnr)
        filetext += "\" [\nlabel=\""
        for item in node.items:
            if item is not None:
                filetext += str(item.item)
                filetext += "|"
        filetext = filetext.strip("|")
        filetext += "\"\nshape=\"record\"\n];\n"
        if node.isLeaf():
            return filetext
        k = -2
        for i in range(node.amount+1):
            filetext += "\n\"node"
            filetext += str(rootnr)
            filetext += "\" -> \"node"
            filetext += str(rootnr*4+k)
            filetext += "\"\n"
            filetext = self.dot(node.children[i], rootnr*4+k, filetext)
            k += 1
        return filetext

    def tableRetrieve(self, searchKey):
        """
        Searches an item with 'searchKey' as its searchkey in the 2-3-4 tree and returns this item.
        Pre: 'searchKey' is of the type KeyType
        Post: if there is an item with 'searchKey' as searchkey in the tree, it gets
        returned, else None is returned
        :param searchKey: searchkey of the item to be found.
        :return: item with 'searchKey' as searchkey and True if item exists, None and False if not.
        """
        return self.retrieve(self.root, searchKey)

    def retrieve(self, node, searchKey):
        """
        Searches an item with 'searchKey' as its searchkey in the 2-3-4 tree, starting at node, and returns this item.
        Pre: 'searchKey' is of the type KeyType
        Post: if there is an item with 'searchKey' as searchkey in the tree, it gets
        returned, else None is returned
        :param node: starting point for search
        :param searchKey: searchkey of the item to be found.
        :return: item with 'searchKey' as searchkey and True if item exists, None and False if not.
        """
        if node is None:
            return None, False
        for item in node.items:
            if item is not None:
                if item.searchKey == searchKey:
                    return item, True
        for x in range(node.amount,0,-1):
            if node.items[x-1].searchKey < searchKey:
                return self.retrieve(node.children[x], searchKey)
        return self.retrieve(node.children[0], searchKey)

    def merge(self, node):
        """
        Makes a 1-node into a 2-node or a 3-node.
        Pre: 'node' is a node from the tree
        Post: 'node' is no longer a 1-node and the tree is still a valid 2-3-4 tree.
        :param node: node that needs to be merged.
        :return: True if node was merged, False if not.
        """
        if node.parent is None or node.amount > 1:
            return False
        if node.allSiblings1Nodes() and node.parent.amount == 1:
            # parent and sibling are 1-nodes so they are merged together to form a 3-node
            sibling = node.getSiblings()[1]
            if not node.isLeaf():
                sibling.children[0].parent = node
                sibling.children[1].parent = node
                node.insertChild(sibling.children[0])
                node.insertChild(sibling.children[1])
            node.insertItem(sibling.deleteItem(sibling.items[0])[0])
            node.insertItem(node.parent.deleteItem(node.parent.items[0])[0])
            node.parent = node.parent.parent
            if node.parent is None:
                self.root = node
            return True
        elif node.allSiblings1Nodes():
            childNr = node.whichChild()
            if childNr == 0:          # node is uiterst linkse kind
                sibling = node.getSiblings()[1]           # rechtse, eerste sibling is enige sibling die we kunnen gebruiken
                parentNr = childNr      # we nemen uiterst linkse item van parent (tussen sibling en node)
            elif (childNr == 1) or (childNr == 2 and node.parent.amount == 3):  # node is een kind in het midden
                sibling = node.getSiblings()[2]        # we nemen rechtse sibling, dus de tweede
                parentNr = childNr      # we nemen parent item tussen node en sibling
            else:                     # node is uiterst rechtse kind
                sibling = node.getSiblings()[1]  # linkse, eerste sibling is enige sibling die we kunnen gebruiken
                parentNr = childNr - 1  # we nemen uiterst rechtse item van parent (tussen sibling en node)
            node.insertItem(sibling.items[0])
            if not node.isLeaf():
                sibling.children[0].parent = node
                sibling.children[1].parent = node
                node.insertChild(sibling.children[0])
                node.insertChild(sibling.children[1])
            node.parent.deleteChild(sibling)
            node.insertItem(node.parent.deleteItem(node.parent.items[parentNr])[0])
            return True
        else:
            if node.getSiblings()[0] == 1:
                sibling = node.getSiblings()[1]
                if node.getMaxSearchKey() < node.getSiblings()[1].getMaxSearchKey():
                    # sibling is rechts van node (node is uiterst links)
                    if not node.isLeaf():
                        sibling.children[0].parent = node
                        node.insertChild(sibling.deleteChild(sibling.children[0])[0])
                    node.insertItem(node.parent.deleteItem(node.parent.items[0])[0])
                    node.parent.insertItem(sibling.deleteItem(sibling.items[0])[0])

                    return True
                else:
                    # sibling is links van node (node is uiterst rechts)
                    if not node.isLeaf():
                        sibling.children[sibling.amount].parent = node
                        node.insertChild(sibling.deleteChild(sibling.children[sibling.amount])[0])
                    node.insertItem(node.parent.deleteItem(node.parent.items[node.parent.amount - 1])[0])
                    node.parent.insertItem(sibling.deleteItem(sibling.items[sibling.amount - 1])[0])
                    return True
            elif node.getSiblings()[2].amount == 1:
                # rechtse sibling heeft maar 1 item, dus we moeten een item nemen uit de linkse sibling
                sibling = node.getSiblings()[1]
                if not node.isLeaf(): # delete child in sibling and add the child in node, change child's parent to node
                    sibling.children[sibling.amount].parent = node
                    node.insertChild(sibling.deleteChild(sibling.children[sibling.amount])[0])
                node.insertItem(node.parent.deleteItem(node.parent.items[sibling.whichChild()])[0]) # insert the item from parent between sibling and node in node
                node.parent.insertItem(sibling.deleteItem(sibling.items[sibling.amount - 1])[0])

                return True
            else:
                # we nemen een item uit de rechtse sibling
                sibling = node.getSiblings()[2]
                if not node.isLeaf():
                    sibling.children[0].parent = node
                    node.insertChild(sibling.deleteChild(sibling.children[0])[0])
                node.insertItem(node.parent.deleteItem(node.parent.items[node.whichChild()])[0])
                node.parent.insertItem(sibling.deleteItem(sibling.items[0])[0])
                return True

    def tableDelete(self, searchKey):
        """
        Deletes the item with 'searchKey' as search key from the 2-3-4 tree, if such item exists.
        Pre: 'searchKey' is of the type KeyType.
        Post: there is no item with 'searchKey' as search key in the 2-3-4 tree and the tree is a valid 2-3-4 tree.
        :param searchKey: search key of the element that needs to be deleted.
        :return: True if deleting was successful, False if not.
        """
        if self.tableIsEmpty() or not self.tableRetrieve(searchKey)[1]:
            return False
        searching = True
        current = self.root
        while searching:
            self.merge(current) # merge is only applied when necessary, no need to check here
            k = 0
            for item in current.items:
                if item is not None:
                    if item.searchKey == searchKey:
                        searching = False
                        if current.isLeaf():
                            current.deleteItem(item)
                            if current.parent is None and current.amount == 0:
                                self.root = None
                            return True
                        else:
                            next = current.children[k+1]
                k += 1
            if searching:
                if searchKey > current.getMaxSearchKey():
                    current = current.children[current.amount]
                else:
                    k = 0
                    for item in current.items:
                        if item.searchKey > searchKey:
                            current = current.children[k]
                            break
                        k += 1
        # searching for inorder successor
        while not next.isLeaf():
            self.merge(next)
            next = next.children[0]
        self.merge(next)

        searching = True
        current = self.root
        while searching:
            k = 0
            for item in current.items:
                if item is not None:
                    if item.searchKey == searchKey:
                        current.deleteItem(item)
                        current.insertItem(next.deleteItem(next.items[0])[0])

                        if next.parent is None and next.amount == 0:
                            self.root = None
                        return True
                k += 1
            if searching:
                if searchKey > current.getMaxSearchKey():
                    current = current.children[current.amount]
                else:
                    k = 0
                    for item in current.items:
                        if item.searchKey > searchKey:
                            current = current.children[k]
                            break
                        k += 1



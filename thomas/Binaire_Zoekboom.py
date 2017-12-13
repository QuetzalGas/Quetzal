from TreeNode import TreeNode


class Binaire_Zoekboom:
    def __init__(self):
        self.root = None

    def __del__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def searchTreeInsert(self, key, newItem, node=None, firsttime=1):
        """
        Inserts a new item in the tree.
        :param node:  The node it has to look for compasiron, will be self.root in the beginning. Used for recursion.
        :param key: The searchkey used to place it in the tree
        :param newItem: Item to be inserted
        :param firsttime: Used to indicate if there was nothing in the tree before. This way a general root is set once.
        :return: Return a node, to adapt the links between the leaves in the tree.
        """
        if node is None:
            node = TreeNode(key, newItem, None, None)
            if firsttime == 1:
                self.root = node
        elif key < node.key:
            node.leftSubTree = self.searchTreeInsert(key, newItem, node.leftSubTree, 0)
        elif key > node.key:
            node.rightSubTree = self.searchTreeInsert(key, newItem, node.rightSubTree, 0)
        elif key == node.key:
            return None
        return node


    def searchTreeRetrieve(self, searchKey):
        """
        Retrieves a sub-tree with the searchKey as root.
        :param searchKey: The key it has to search for
        :return: If the key is in the tree, it returns the node with that searchkey. Else None is returned.
        """
        dict = self.inorderTraverse(self.root)
        for i,j in dict.items():
            if j == searchKey:
                node = i
                break
            else:
                node = None
        return node


    def inorderTraverse(self, node, dict=None):
        """
        Traverses the tree following the inorder algorithm.
        :param: node: The node it has to start with.
        :param: array: The array of elements it visited.
        :return: A list of the items in the order the algorithm has visited them.
        """
        if dict is None:
            dict = {}
        if node is None:
            return None
        self.inorderTraverse(node.leftSubTree, dict)
        dict[node] = node.key
        self.inorderTraverse(node.rightSubTree, dict)
        return dict

    def print(self):
        """
        Prints the whole tree in sorted manner.
        """
        inorder = self.inorderTraverse(self.root)
        #Invert the dictionary
        inv_inorder = {k: l for l, k in inorder.items()}
        for i, j in inv_inorder.items():
            print(i)

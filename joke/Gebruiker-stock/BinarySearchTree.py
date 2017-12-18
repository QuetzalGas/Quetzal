class TreeItem:
    def __init__(self,item, searchKey, leftTree=None, rightTree=None ):
        self.item = item
        self.searchKey = searchKey
        self.leftTree = leftTree
        self.rightTree = rightTree

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def destroySearchTree(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def searchTreeInsert(self, newItem):
        newNode = TreeItem(newItem, newItem)
        if self.root is None:
            self.root = newNode
        else:
            treePtr = self.root
            while treePtr is not None:
                if newNode.searchKey < treePtr.searchKey:
                    if treePtr.leftTree is None:
                        treePtr.leftTree = newNode
                        return True
                    treePtr = treePtr.leftTree
                elif newNode.searchKey > treePtr.searchKey:
                    if treePtr.rightTree is None:
                        treePtr.rightTree = newNode
                        return True
                    treePtr = treePtr.rightTree
                elif newNode.searchKey == treePtr.searchKey:
                    return False




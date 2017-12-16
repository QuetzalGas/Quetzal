class TreeItem:
    def __init__(self, item, key):
        self.item = item
        self.key = key


class BinarySearchTree:
    def __init__(self, root, left=None, right=None):
        """
        Een nieuwe binaire boom wordt geïnitialiseerd.
        :param root: de wortel van de binaire zoekboom
        :param left: het linkerkind van de boom, dat oftewel None is, oftewel ook een binaire zoekboom
        :param right: het rechterkind: oftewel None oftewel ook binaire zoekboom
        """
        self.root = root
        self.left = left
        self.right = right

    def destroy(self):
        del self

    def isEmpty(self):
        """
        Checkt of de binaire boom leeg is.
        :return: geeft True indien leeg, False indien niet leeg.
        """
        if self.left is None and self.right is None:
            return True
        else:
            return False

    def searchTreeInsert(self, item):
        """
        Voegt nieuw TreeNode toe aan binaire zoekboom, op de juiste plaats, als er nog geen item met dezelfde zoeksleutel aanwezig is.
        :param item: een TreeNode
        :return: geeft True indien de zoeksleutel van de TreeNode nog niet aanwezig was,
                geeft False indien het wel al aanwezig was.
        """
        if item.key < self.root.key:
            if self.left is None:
                self.left = BinarySearchTree(item)
                return True
            else:
                return self.left.searchTreeInsert(item)
        elif item.key > self.root.key:
            if self.right is None:
                self.right = BinarySearchTree(item)
                return True
            else:
                return self.right.searchTreeInsert(item)
        if item.key == self.root.key:
            return False


    def searchTreeRetrieve(self, key):
        """
        Indien een item met de gevraagde zoeksleutel aanwezig is, wordt de (sub)binaire zoekboom met de zoeksleutel teruggegeven.
        :param key: de zoeksleutel, waarnaar eerst gezocht wordt
        :return: geeft de (sub) binaire boom terug als er een TreeNode met de zoeksleutel aanwezig is, anders geeft het False terug
        """
        if key < self.root.key and self.left is not None:
            return self.left.searchTreeRetrieve(key)
        elif key > self.root.key and self.right is not None:
            return self.right.searchTreeRetrieve(key)
        if key == self.root.key:
            return (True, self.root)
        else:
            return (False, None)

    def inorderTraverse(self):
        listInorder = list()
        if self.left is not None:
            return listInorder.append(self.left.inorderTraverse())
        listInorder.append(self.root.item)
        if self.right is not None:
            return listInorder.append(self.right.inorderTraverse())

    def print(self):
        """
        Print de zoeksleutels van de TreeNodes in inorderTraverse.
        """
        if self.left is not None:
            self.left.inorderTraverse()
        print(self.root.key)
        if self.right is not None:
            self.right.inorderTraverse()


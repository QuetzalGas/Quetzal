class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.content = None

    def search(self, key):
        if self.key == key:
            return self
        elif self.left is not None and key < self.key:
            return self.left.search(key)
        elif self.right is not None:
            return self.right.search(key)
        else:
            return self

    def insert(self, item, key):
        if self.content is None:
            self.content = (item, key)
            self.left = Node()
            self.right = Node()
        elif key < self.content[1]:
            self.left.insert(item, key)
        else:
            self.right.insert(item, key)

    def delete(self, key):
        if self.content is None:
            return False

    def is_leaf(self):
        if self.content is None:
            return False
        elif self.left.content is None and self.right.content is None:
            return True
        else:
            return False

    def traverseInorder(self, visit):
        if self.content is None:
            return

        if self.left.content is not None:
            self.left.traverseInorder(visit)

        visit(self.content[0])

        if self.right.content is not None:
            self.right.traverseInorder(visit)


    def traversePreorder(self, visit):
        if self.content is None:
            return

        visit(self.content[0])

        if self.left.content is not None:
            self.left.traverseInorder(visit)

        if self.right.content is not None:
            self.right.traverseInorder(visit)


    def traversePostorder(self, visit):
        if self.content is None:
            return

        if self.left.content is not None:
            self.left.traverseInorder(visit)

        if self.right.content is not None:
            self.right.traverseInorder(visit)

        visit(self.content[0])


    def dot(self, c=0):
        if self.content is None:
            return None

        output = ''

        if self.left.content is not None:
            output += '  {}->{}\n'.format(self.content[0], self.left.content[1])
            output += self.left.dot(c+1) 
            c = c+1
        else:
            output += '  nul{} [style="invisible"]\n'.format(c)
            output += '  {}->nul{} [style="invisible"]\n'.format(self.content[0], c)

        if self.right.content is not None:
            output += '  {}->{}\n'.format(self.content[0], self.right.content[1])
            output += self.right.dot(c+1)
            c = c+1
        else:
            output += '  nul{} [style="invisible"]\n'.format(c)
            output += '  {}->nul{} [style="invisible"]\n'.format(self.content[0], c)

        return output


class BinarySearchTree(Node):
    def __init__(self):
        Node.__init__(self)

    def isEmpty(self):
        return self.content is None

class FusedIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.fuse = False

    def __next__(self):
        if self.fuse:
            raise StopIteration
        else:
            self.fuse = True
            return self.iterator.__next__()

class InorderIterator:
    def __init__(self, root):
        self.step = 0

        if root is not None:
            self.root = root.__iter__()
            self.left = InorderIterator(root.left)
            self.right = InorderIterator(root.right)
        else:
            self.root = None
            self.left = None
            self.right = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.step == 0:
            if self.left is None:
                # No left child: look at root
                self.step = 1
            else:
                try:
                    return self.left.__next__()
                except StopIteration:
                    # If the left subtree is done, look at the root
                    self.step = 1

        if self.step == 1:
            if self.root is None:
                # If there is no root, we can stop iteration.
                raise StopIteration
            else:
                try:
                    return self.root.__next__()
                except StopIteration:
                    self.step = 2

        if self.step == 2:
            if self.right is None:
                raise StopIteration
            else:
                return self.right.__next__()

        raise StopIteration

class PreorderIterator:
    def __init__(self, root):
        self.step = 0

        if root is not None:
            self.root = root.__iter__()
            self.left = PreorderIterator(root.left)
            self.right = PreorderIterator(root.right)
        else:
            self.root = None
            self.left = None
            self.right = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.step == 0:
            if self.root is None:
                # If there is no root, we can stop iteration.
                raise StopIteration
            else:
                try:
                    return self.root.__next__()
                except StopIteration:
                    # If the root is done, look at the left subtree
                    self.step = 1

        if self.step == 1:
            if self.left is None:
                raise StopIteration
            else:
                try:
                    return self.left.__next__()
                except StopIteration:
                    self.step = 2

        if self.step == 2:
            if self.right is None:
                raise StopIteration
            else:
                return self.right.__next__()

        raise StopIteration

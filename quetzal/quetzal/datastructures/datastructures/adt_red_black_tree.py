from .adt_iterators import FusedIterator, InorderIterator, PreorderIterator

class Node:
    def __init__(self, key, content):
        self.key = key

        if content is None:
            self.content = None
        else:
            self.content = [content]

        self.black = False
        self.left = None
        self.right = None
        self.parent = None

    def is_color_valid(self):
        """ Validate color combination.
        :return: True if valid, False otherwise.
        """
        if self.black:
            if (self.left is None) and (self.right is None):
                # A black leaf node is OK.
                return True
            elif (self.left is not None) and (self.right is not None):
                # A black node with two children has no restriction on the
                # colors of the children
                return True
            elif (self.left is None) and (self.right is not None):
                # If only right child, that child must be red.
                return not self.right.black
            else:
                # If only left child, that child must be red.
                return not self.left.black
        else:
            if (self.left is None) and (self.right is None):
                # A red leaf node is OK.
                return True
            elif (self.left is not None) and (self.right is not None):
                # Both children of a red node must be black.
                return self.left.black and self.right.black
            else:
                # A red node must have either zero, or two children.
                return False

    def is_child_relation_valid(self):
        if self.left is not None:
            if not (self.left.parent == self):
                return False

        if self.right is not None:
            if not (self.right.parent == self):
                return False

        return True

    def is_node_valid(self):
        return self.is_color_valid() and self.is_child_relation_valid()

    def __iter__(self):
        return FusedIterator(self)

    def __next__(self):
        # for the iterator
        return (self.key, self.content, self.black)

    def is_black(self):
        return self.black

    def is_red(self):
        return not self.black

    def is_four_node_root(self):
        return (self.left is not None and not self.left.black) and\
               (self.right is not None and not self.right.black)

    def flip_color(self):
        self.black = not self.black
        self.left.black = not self.left.black
        self.right.black = not self.right.black

    def is_two_node(self):
        if not self.black:
            return False

        # Change this to be more inclusive

        if (self.left is None) and (self.right is None):
            return True

        return (self.left is not None and self.left.black) and\
               (self.right is not None and self.right.black)

    def is_left_child(self):
        return (self.parent is not None) and (self.parent.left == self)

    def is_right_child(self):
        return (self.parent is not None) and (self.parent.right == self)

    def set_right_child(self, child):
        previous = self.right

        self.right = child
        if self.right is not None:
            self.right.parent = self

        if previous is not None:
            previous.parent = None

        return previous

    def rotate_left(self):
        """ Rotate this node to the left, and return the highest node after rotation.

        A rotation is a local O(1) operation that restructures nodes such that
        one subtree gets closer the root, and another subtree gets one level
        further from the root. This operation preserves the in-order property
        of the RB-tree.

        This is used to transform a right leaning 3-node to a left leaning 3-
        node.

             |                     |
            self                   x
           /    \                 / \ 
          a      x    =>      self   c
                / \          /    \ 
               b   c        a      b
        """
        parent = self.parent

        if self.right is None:
            raise RuntimeError("Can't rotate right.")

        x = self.right

        self.right = x.left

        if self.right is not None:
            self.right.parent = self

        x.left = self

        if x.left is not None:
            x.left.parent = x

        x.parent = parent
        if parent is not None:
            if parent.left == self:
                parent.left = x
            elif parent.right == self:
                parent.right = x
            else:
                raise RuntimeError("Invariant broken")

        (x.black, self.black) = (self.black, x.black)

        return x

    def rotate_right(self):
        """
              |              |
             self            x
            /    \          / \ 
           x      c   =>   a   self
          / \                 /    \ 
         a   b               b      c
        """
        parent = self.parent

        if self.left is None:
            raise RuntimeError("Can't rotate right: no left child")

        x = self.left

        self.left = x.right

        if self.left is not None:
            self.left.parent = self

        x.right = self

        if x.right is not None:
            x.right.parent = x

        x.parent = parent
        if parent is not None:
            if parent.left == self:
                parent.left = x
            elif parent.right == self:
                parent.right = x
            else:
                raise RuntimeError("Invariant broken")

        (x.black, self.black) = (self.black, x.black)

        return x

    def set_left_child(self, child):
        previous = self.left

        self.left = child
        if self.left is not None:
            self.left.parent = self

        if previous is not None:
            previous.parent = None

        return previous

    def find_root(self):
        root = self

        while root.parent is not None:
            root = root.parent

        return root


    def split(self):
        """ Split four nodes
        """
        if not self.is_four_node_root():
            return

        if self.parent is None:
            # Root
            self.flip_color()
            self.black = True
        else:
            if self.parent.is_two_node():
                self.flip_color()
            else:
                # 3-node parent
                if self.is_left_child():
                    if self.parent.black:
                        self.flip_color()
                    elif self.parent.is_left_child():
                        self.parent.parent.rotate_right()
                        self.flip_color()
                    else:
                        self.flip_color()
                        self.parent.rotate_right()
                        self.parent.rotate_left()
                else:
                    # We are a right child.
                    if self.parent.black:
                        self.flip_color()
                    elif self.parent.is_right_child():
                        self.parent.parent.rotate_left()
                        self.flip_color()
                    else:
                        self.flip_color()
                        self.parent.rotate_left()
                        self.parent.rotate_right()

    def fix_4_node(self):
        """ Fix four-nodes.

           (a)    (b)    (c)    (d)
              3  1       1        3
             /    \       \      /
            2      2       3    1
           /        \     /      \ 
          1          3   2        2

        Restructure to:
            2
           / \ 
          1   3
        """
        # When called, we know that the recently added node must be red.

        if self.parent is None:
            # Can't happen actually....
            raise RuntimeError('Impossible....')

        if self.parent.black:
            # If the parent is black, we have a valid 4 node.
            return

        t_left = self.is_left_child()
        p_left = self.parent.is_left_child()

        if t_left and p_left:
            # (a)
            self.parent.parent.rotate_right()
        elif not t_left and not p_left:
            # (b)
            self.parent.parent.rotate_left()
        elif t_left and not p_left:
            # (c)
            self.parent.rotate_right()
            self.parent.rotate_left()
        elif not t_left and p_left:
            # (d)
            self.parent.rotate_left()
            self.parent.rotate_right()

    def insert(self, key, content):
        self._insert(key, content)

        root = self.find_root()
        root.black = True

        return root

    def _insert(self, key, content):
        if self.key is None:
            # If this node is empty, we set the content and the key to the
            # inserted values.
            self.key = key
            self.content = [content]
            return

        # All four-nodes must be split first. We can take a small shortcut in
        # some two scenario's if we explicitly store the left and right
        # subtrees before we split.
        left = self.left
        right = self.right
        self.split()

        if key == self.key:
            self.content.append(content)
        elif key > self.key:
            if right is None:
                self.set_right_child(Node(key, content))
                self.right.fix_4_node()
            else:
                right._insert(key, content)
        elif key < self.key:
            if left is None:
                self.set_left_child(Node(key, content))
                self.left.fix_4_node()
            else:
                left._insert(key, content)

    def combine(self):
        # Root nodes can not be combined.
        if self.parent is None:
            return

        # Skip all non two nodes.
        if not self.is_two_node():
            return

        if self.parent.is_two_node():
            is_left = self.is_left_child()
            # Get sibling
            if is_left:
                sibling = self.parent.right
            else:
                sibling = self.parent.left

            # Sanity check...
            if sibling is None:
                raise RuntimeError('Two node with only one child.')

            # Two node
            if sibling.is_two_node():
                # Create a four node.
                self.parent.flip_color()
                self.parent.black = True
                return

            # Four node
            if sibling.is_four_node_root():
                if is_left:
                    sibling.rotate_right()
                    # self.parent.rotate_left()
                else:
                    top = sibling.rotate_left()
                    top.left.black = True
                    self.parent.rotate_right()

                return

            # Three node

    def delete(self, key):
        self.combine()

        if self.key == key:
            return True

        if (self.left is not None) and (key < self.key):
            return self.left.delete(key)
        elif (self.right is not None) and (key > self.key):
            return self.right.delete(key)

        return False

    def print(self, filename):
        with open(filename, 'w') as of:
            of.write('digraph rb {\n')
            of.write('  node[shape = record];\n')
            out = self.dot()
            of.write(out[0])
            of.write('}')

    def add_dummy_leaves(self, tag):
        if self.left is None:
            self.left = Node(tag, tag)
            self.left.black = True
            tag = chr(ord(tag) + 1)
        else:
            tag = self.left.add_dummy_leaves(tag)

        if self.right is None:
            self.right = Node(tag, tag)
            self.right.black = True
            tag = chr(ord(tag) + 1)
        else:
            tag = self.right.add_dummy_leaves(tag)

        return tag

    def height_234(self, h):
        left_height = h
        right_height = h

        if self.left is not None:
            if self.left.black:
                k = 1
            else:
                k = 0

            left_height = self.left.height_234(h + k)

        if self.right is not None:
            if self.right.black:
                k = 1
            else:
                k = 0

            right_height = self.right.height_234(h + k)

        return max(left_height, right_height)

    def dot(self, c=0):
        if self.content is None:
            return None

        if self.black:
            output = '  node{}[label = "<l>|<m> {}: {}|<r>"];\n'.format(
                c, self.key, self.content)
        else:
            output = '  node{}[label = "<l>|<m> {}: {}|<r>", color=red];\n'.format(
                c, self.key, self.content)

        root = c

        if (self.left is not None) and (self.left.content is not None):
            (o2, c) = self.left.dot(c + 1)
            output += o2

            if self.left.black:
                output += '  "node{}":l->"node{}":m;\n'.format(root, root + 1)
            else:
                output += '  "node{}":l->"node{}":m [color=red];\n'.format(
                    root, root + 1)
        else:
            output += '  node{} [style="invisible"];\n'.format(root + 1)
            output += '  "node{}":l->node{} [style="invisible"];\n'.format(
                root, root + 1)
            c = c + 1

        if (self.right is not None) and (self.right.content is not None):
            c_plus = c + 1
            (o2, c) = self.right.dot(c_plus)
            output += o2

            if self.right.black:
                output += '  "node{}":r->"node{}":m;\n'.format(root, c_plus)
            else:
                output += '  "node{}":r->"node{}":m [color=red];\n'.format(
                    root, c_plus)

        else:
            output += '  node{} [style="invisible"];\n'.format(c + 1)
            output += '  "node{}":r->node{} [style="invisible"];\n'.format(
                root, c + 1)
            c = c + 1

        return (output, c + 1)

class AdtRedBlackTree:
    def __init__(self):
        self.root = Node(None, None)
        self.root.black = True

    def insert(self, key, content=None):
        if content is None:
            self.root = self.root.insert(key, key)
        else:
            self.root = self.root.insert(key, content)

        self.root.black = True

    def delete(self, key):
        self.root.delete(key)

        while self.root.parent is not None:
            self.root = self.root.parent

    def dot(self, filename, label):
        with open(filename, 'w') as of:
            of.write('digraph rb {\n')
            of.write('  node[shape = record];\n')
            out = self.root.dot()
            of.write(out[0])
            of.write('  labelloc="t";\n')
            of.write('  label="{}";\n'.format(label))
            of.write('}')

    def iter_inorder(self):
        return InorderIterator(self.root)

    def iter_preorder(self):
        return PreorderIterator(self.root)

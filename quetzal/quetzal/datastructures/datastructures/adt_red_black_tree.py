from .adt_iterators import FusedIterator, InorderIterator, PreorderIterator
from .adt_stack import AdtStack

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

    def __getitem__(self, key):
        if key == self.key:
            return self
        elif (self.left is not None) and (key < self.key):
            return self.left[key]
        elif (self.right is not None):
            return self.right[key]
        else:
            raise KeyError

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

    def get_children(self):
        if not self.black:
            return self.parent.get_children()

        if self.is_two_node():
            return (self.left, self.right)

        if self.is_root_of_four_node():
            return (self.left.left, self.left.right, self.right.left, self.right.right)

        if self.is_root_of_three_node():
            if self.is_left_leaning():
                return (self.left.left, self.left.right, self.right)
            else:
                return (self.left, self.right.left, self.right.right)

    def get_nearest_sibling(self):
        """ Return the nearest sibling of a node.

        By convention, we define the nearest sibling to be the left sibling,
        unless the node is the left-most child, in which case the nearest
        sibling is to the right.
        """
        children = self.parent.get_children()

        if len(children) == 2:
            (l, r) = children

            if self == l:
                return r
            else:
                return l

        if len(children) == 3:
            (s, m, l) = children

            if self == l:
                return m
            if self == m:
                return s
            if self == s:
                return m

        if len(children) == 4:
            (xs, s, l, xl) = children

            if self == xl:
                return l
            elif self == l:
                return s
            elif self == s:
                return xs
            elif self == xs:
                return s

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

    def is_left_leaning(self):
        return (self.left is not None) and (not self.left.black)

    def make_left_leaning(self):
        if self.is_root_of_three_node():
            if not self.is_left_leaning():
                return self.rotate_left()
        elif self.is_tail_of_three_node():
            return self.parent.make_left_leaning()

        return self

    def is_right_leaning(self):
        return (self.right is not None) and (not self.right.black)

    def make_right_leaning(self):
        if self.is_root_of_three_node():
            if not self.is_right_leaning():
                return self.rotate_right()
        elif self.is_tail_of_three_node():
            return self.parent.make_right_leaning()

        return self

    def is_root_of_three_node(self):
        l_red = (self.left is not None) and (not self.left.black)
        r_red = (self.right is not None) and (not self.right.black)

        return self.black and ((l_red and not r_red) or (r_red and not l_red))

    def is_tail_of_three_node(self):
        if self.parent is None:
            return False

        return self.parent.is_root_of_three_node() and (not self.black)

    def is_three_node(self):
        return (self.is_tail_of_three_node() or self.is_root_of_three_node())

    def is_root_of_four_node(self):
        l_ok = (self.left is not None) and (not self.left.black)
        r_ok = (self.right is not None) and (not self.right.black)

        return (self.black and l_ok and r_ok)

    def is_tail_of_four_node(self):
        if self.parent is None:
            return False

        return self.parent.is_root_of_four_node() and (not self.black)

    def is_four_node(self):
        return (self.is_tail_of_four_node() or self.is_root_of_four_node())

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

        return (self.left and self.left.black) and\
               (self.right and self.right.black)

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
        if not self.is_root_of_four_node():
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

    def balance_four_node(self):
        """ Balance a four-node.

           (a)    (b)    (c)    (d)
              3  1       1        3
             .    .       .      .
            2      2       3    1
           .        .     .      . 
          1          3   2        2

        Restructure to:
            2
           . . 
          1   3
        """
        # When called, we know that the recently added node must be red.

        if self.parent is None:
            # Can't happen actually....
            raise RuntimeError('Impossible....')

        if self.parent.black:
            # If the parent is black we have a three node, and thus there is
            # nothing to balance.
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
                self.right.balance_four_node()
            else:
                right._insert(key, content)
        elif key < self.key:
            if left is None:
                self.set_left_child(Node(key, content))
                self.left.balance_four_node()
            else:
                left._insert(key, content)

    def combine_if_necessary(self):
        # Root nodes can not be combined.
        if self.parent is None:
            return

        # Skip all non two nodes.
        if not self.is_two_node():
            return

        if self.parent.is_two_node():
            self._combine_parent_two_node()
        elif self.parent.is_three_node():
            self._combine_parent_three_node()
        elif self.parent.is_four_node():
            self._combine_parent_four_node()

    def _combine_parent_two_node(self):
        is_left = self.is_left_child()
        # Get sibling
        if is_left:
            sibling = self.parent.right
        else:
            sibling = self.parent.left

        # Sanity check...
        if sibling is None:
            raise RuntimeError('Two node with only one child.')

        if sibling.is_two_node():
            # This case is easy, we just have to flip colors.
            self.parent.flip_color()
            self.parent.black = True
        elif sibling.is_root_of_four_node():
            if is_left:
                sibling.rotate_right()
                sibling.black = True

                self.parent.rotate_left()
                self.black = False
            else:
                sibling.rotate_left()
                sibling.black = True

                self.parent.rotate_right()
                self.black = False
        elif sibling.is_root_of_three_node():
            # Three node
            if is_left:
                sibling = sibling.make_right_leaning()
                sibling.right.black = True
                self.parent.rotate_left()
            else:
                sibling = sibling.make_left_leaning()
                sibling.left.black = True
                self.parent.rotate_right()

            self.black = False
        else:
            raise RuntimeError('dd')

    def _combine_parent_three_node(self):
        (s, m, l) = self.parent.get_children()
        nearest_sibling = self.get_nearest_sibling()

        if self == l:
            if nearest_sibling.is_two_node():
                # Merge
                self.parent.make_right_leaning()
                self.parent.flip_color()
            elif nearest_sibling.is_root_of_three_node():
                # Redistribute
                self.parent.make_right_leaning()

                sibling = nearest_sibling.make_left_leaning()
                sibling.left.black = True

                self.parent.rotate_right()
                self.black = False
                # This balances the tree, and is optional
                self.parent.parent.make_left_leaning()
            elif nearest_sibling.is_root_of_four_node():
                # Redistribute
                self.parent.make_right_leaning()
                nearest_sibling.rotate_left()
                nearest_sibling.black = True

                self.parent.rotate_right()
                self.black = False

                self.parent.parent.make_left_leaning()
        elif self == m:
            if nearest_sibling.is_two_node():
                # Merge
                self.parent.make_left_leaning()
                self.parent.flip_color()
            elif nearest_sibling.is_root_of_three_node():
                self.parent.make_left_leaning()

                sibling = nearest_sibling.make_left_leaning()
                sibling.left.black = True

                self.parent.rotate_right()
                self.black = False

                self.parent.parent.make_right_leaning()
            elif nearest_sibling.is_root_of_four_node():
                self.parent.make_left_leaning()

                nearest_sibling.rotate_left()
                nearest_sibling.black = True

                self.parent.rotate_right()
                self.black = False

                self.parent.parent.make_right_leaning()
        elif self == s:
            if nearest_sibling.is_two_node():
                # Merge
                self.parent.make_left_leaning()
                self.parent.flip_color()
            elif nearest_sibling.is_root_of_three_node():
                self.parent.make_left_leaning()

                sibling = nearest_sibling.make_right_leaning()
                sibling.right.black = True

                self.parent.rotate_left()
                self.black = False
                
                self.parent.parent.make_right_leaning()
            elif nearest_sibling.is_root_of_four_node():
                self.parent.make_left_leaning()

                nearest_sibling.rotate_right()
                nearest_sibling.black = True

                self.parent.rotate_left()
                self.black  = False

                self.parent.parent.make_right_leaning()

    def _combine_parent_four_node(self):
        (xs, s, l, xl) = self.parent.get_children()
        nearest_sibling = self.get_nearest_sibling()

        if self == xl:
            if nearest_sibling.is_two_node():
                # Merge case 1
                self.parent.flip_color()
            else:
                # Cases 1 and 2
                self._combine_parent_two_node()
        elif self == l:
            if nearest_sibling.is_two_node():
                # Merge case 2
                # Reverse from split
                self.parent.parent.rotate_right()
                self.parent.parent.rotate_left()
                self.parent.flip_color()
            elif nearest_sibling.is_root_of_three_node():
                # Case 3
                sibling = nearest_sibling.make_right_leaning()
                sibling.right.black = True
                sibling.parent.rotate_left()
                sibling = sibling.rotate_left()
                sibling.left.rotate_right()

                sibling.left.black = False

                # We are done with the left subtree.
                sibling.parent.right.rotate_right()

                # Now we are at the root
                root = sibling.parent.rotate_right()

                # We only need to rotate the right subtree twice.
                root.right.rotate_left()
                root.right.rotate_left()
            elif nearest_sibling.is_root_of_four_node():
                # Case 4
                sibling = nearest_sibling.rotate_left()
                sibling.left.black = True
                sibling.parent.rotate_left()
                sibling.left.black = False

                self.parent.rotate_right()
                root = sibling.parent.rotate_right()
                root.right.rotate_left()
                root.right.rotate_left()
        elif self == s:
            if nearest_sibling.is_two_node():
                # Merge case 3
                self.parent.flip_color()
            else:
                # Cases 5 and 6
                self._combine_parent_two_node()
        elif self == xs:
            if nearest_sibling.is_two_node():
                # Merge case 4
                self.parent.flip_color()
            else:
                # Cases 7 and 8
                self._combine_parent_two_node()

    def combine_towards_inorder_successor(self):
        if not (self.right and self.left):
            # This can only happen if we start in a three node that doesn't
            # have any children, so we also don't have an inorder successor
            # to find.
            return None

        if self.right:
            # Where we start is subtle: we need to consider three nodes.
            if self.right.black:
                start = self.right
            else:
                start = self.right.left

            if start:
                # We have a right subtree, so let's keep going to the left.
                current = start

                future_left = current.left
                current.combine_if_necessary()

                while future_left:
                    current = future_left
                    future_left = current.left
                    current.combine_if_necessary()

                if current.is_two_node():
                    raise RuntimeError('should not be possible')

                # This will make it easy to delete the node if the inorder
                # successor is a three node.
                if current.is_three_node():
                    current.make_left_leaning()

                return current
            else:
                # This happens when we try to search from a three-node leaf.
                return None

    def delete(self, key):
        self.combine_if_necessary()

        if self.key == key:
            if len(self.content) > 1:
                # If we store multiple items with the same key, we only
                # remove the first one in the list
                self.content.pop(0)
                return self
            else:
                successor = self.combine_towards_inorder_successor()
                
                if successor:
                    # We do not explicitly swap, but we only copy the
                    # content and the key from the successor.
                    self.key, self.content = successor.key, successor.content

                    return successor.delete_non_empty_leaf()
                else:
                    self.key = None
                    self.content = None

                    return self.delete_non_empty_leaf()
        elif self.left and (key < self.key):
            return self.left.delete(key)
        elif self.right and (key > self.key):
            return self.right.delete(key)
        else:
            raise KeyError

    def delete_non_empty_leaf(self):
        if self.is_two_node():
            # Nothing to do if we are a two node.
            return self

        if not self.black:
            if self.left or self.right:
                raise RuntimeError('not deleting from a leaf')

        new_root = self.parent

        if self.is_tail_of_four_node():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None

            self.parent = None
        else:
            if self.is_root_of_three_node():
                # This will make `self` a tail of a three node.
                if self.is_left_leaning():
                    self.rotate_right()
                else:
                    self.rotate_left()

            elif self.is_root_of_four_node():
                self.rotate_right()
                self.rotate_left()

            new_root = self.parent

            # We don't actually care which one we are, because both need to
            # be None in a leaf.
            self.parent.left = None
            self.parent.right = None
            self.parent = None

        return new_root

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

    def height_234(self, h = 0):
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

        if left_height != right_height:
            raise RuntimeError('Unequal heights')

        return left_height

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

    def __getitem__(self, key):
        raise KeyError
        return self.root[key].content[0]
    
    def __contains__(self, key):
        try:
            self.root[key]

            return True
        except KeyError:
            return False

    def __setitem__(self, key, value):
        self.root = self.root.insert(key, value)
        self.root.black = True

    def __delitem__(self, key):
        root = self.root.delete(key)
        self.root = root.find_root()
        self.root.black = True

    def from_deser(self, preorder, red_nodes):
        stack = AdtStack()

        self.root = Node(preorder[0], preorder[0])
        self.root.black = True
        stack.push(self.root)

        for i in preorder[1:]:
            temp = None

            while (not stack.is_empty()) and (i > stack.peek().key):
                temp = stack.pop_and_return()

            child = Node(i, i)

            if i not in red_nodes:
                child.black = True

            if temp is not None:
                temp.set_right_child(child)
            else:
                temp = stack.peek()
                temp.set_left_child(child)

            stack.push(child)

    def __repr__(self):
        return self.root.dot()

    def dot(self, filename, label):
        with open(filename, 'w') as of:
            of.write('digraph rb {\n')
            of.write('  node[shape = record];\n')
            out = self.root.dot()
            of.write(out[0])
            of.write('  labelloc="t";\n')
            of.write('  label="{}";\n'.format(label))
            of.write('}')

    def __iter__(self):
        return self.iter_inorder()

    def iter_inorder(self):
        return InorderIterator(self.root)

    def iter_preorder(self):
        return PreorderIterator(self.root)

class Node:
    def __init__(self, key, content):
        self.key = key
        self.content = content
        self.black = False
        self.left = None
        self.right = None
        self.parent = None

    def is_black(self):
        return self.black

    def is_red(self):
        return not self.black

    def is_four_node(self):
        return (self.left is not None and not self.left.black) and\
               (self.right is not None and not self.right.black)

    def flip_color(self):
        self.black = not self.black
        self.left.black = not self.left.black
        self.right.black = not self.right.black

    def is_two_node(self):
        if not self.black:
            return False

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

        This is used to rotate a right leaning 3-node to a left leaning 3-
        node.

            self                           x
         a        x          =>      self       c
               b     c            a        b
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

        x.black = self.black
        self.black = False
        return x

    def rotate_right(self):
        """
               self           x
            x        c  => a     self
         a     b              b        c
        """
        parent = self.parent

        if self.left is None:
            raise RuntimeError("Can't rotate right")

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

        x.black = self.black
        self.black = False
        return x


    def set_left_child(self, child):
        previous = self.left

        self.left = child
        if self.left is not None:
            self.left.parent = self

        if previous is not None:
            previous.parent = None

        return previous

    def split(self):
        if not self.is_four_node():
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
        # When called, we know that the recently added node must be red.

        # Root
        if self.parent is None:
            # Can't happen actually....
            return

        # Not a four node.
        if self.parent.black:
            return

        t_left = self.is_left_child()
        p_left = self.parent.is_left_child()

        if t_left and p_left:
            self.parent.parent.rotate_right()
        elif not t_left and not p_left:
            self.parent.parent.rotate_left()
        elif t_left and not p_left:
            self.parent.rotate_right()
            self.parent.rotate_left()
        elif not t_left and p_left:
            self.parent.rotate_left()
            self.parent.rotate_right()


    def insert(self, key, content):
        if self.key is None:
            self.key = key
            self.content = content
            return self

        self.split()

        if key > self.key:
            if self.right is None:
                self.set_right_child(Node(key, content))
                self.right.fix_4_node()
            else:
                self.right.insert(key, content)
        elif key < self.key:
            if self.left is None:
                self.set_left_child(Node(key, content))
                self.left.fix_4_node()
            else:
                self.left.insert(key, content)

        root = self

        while root.parent is not None:
            root = root.parent

        root.black = True
        return root


    def delete(self, key):
        pass


    def print(self, filename):
        with open(filename, 'w') as of:
            of.write('digraph rb {\n')
            of.write('  node[shape = record];\n')
            out = self.dot()
            of.write(out[0])
            of.write('}')


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

    def balanced_234(self, h):
        pass

    def dot(self, c=0):
        if self.content is None:
            return None

        if self.black:
            output = '  node{}[label = "<l>|<m> {}|<r>"];\n'.format(c, self.content)
        else:
            output = '  node{}[label = "<l>|<m> {}|<r>", color=red];\n'.format(c, self.content)

        root = c

        if (self.left is not None) and (self.left.content is not None):
            (o2, c) = self.left.dot(c+1) 
            output += o2

            if self.left.black:
                output += '  "node{}":l->"node{}":m;\n'.format(root, root+1)
            else:
                output += '  "node{}":l->"node{}":m [color=red];\n'.format(root, root+1)
        else:
            output += '  node{} [style="invisible"];\n'.format(root+1)
            output += '  "node{}":l->node{} [style="invisible"];\n'.format(root, root+1)
            c = c+1

        if (self.right is not None) and (self.right.content is not None):
            c_plus = c+1
            (o2, c) = self.right.dot(c_plus)
            output += o2

            if self.right.black:
                output += '  "node{}":r->"node{}":m;\n'.format(root, c_plus)
            else:
                output += '  "node{}":r->"node{}":m [color=red];\n'.format(root, c_plus)

        else:
            output += '  node{} [style="invisible"];\n'.format(c+1)
            output += '  "node{}":r->node{} [style="invisible"];\n'.format(root, c+1)
            c = c+1

        return (output, c+1)


class RbTree:
    def __init__(self):
        self.root = Node(None, None)
        self.root.black = True

    def insert(self, key, content = None):
        if content is None:
            self.root = self.root.insert(key, key)
        else:
            self.root = self.root.insert(key, content)

        self.root.black = True

    def dot(self, filename, label):
        with open(filename, 'w') as of:
            of.write('digraph rb {\n')
            of.write('  node[shape = record];\n')
            out = self.root.dot()
            of.write(out[0])
            of.write('  labelloc="t";\n')
            of.write('  label="{}";\n'.format(label))
            of.write('}')
        

def standard(offset = 0):
    a = Node(offset + 0, "a")
    a.black = True
    b = Node(offset + 2, "b")
    b.black = True
    c = Node(offset + 4, "c")
    c.black = True
    d = Node(offset + 6, "d")
    d.black = True

    S = Node(offset + 1, "S")
    S.set_left_child(a)
    S.set_right_child(b)

    L = Node(offset + 5, "L")
    L.set_left_child(c)
    L.set_right_child(d)

    M = Node(offset + 3, "M")
    M.black = True
    M.set_left_child(S)
    M.set_right_child(L)

    return M

def b2():
    M = standard()

    e = Node("e")
    P = Node("P")
    P.set_right_child(e)
    P.set_left_child(M)

    return P

def b4():
    M = standard()

    e = Node("e")
    f = Node("f")
    P = Node("P")
    P.set_right_child(e)
    P.set_left_child(M)
    P.black = False
    Q = Node("Q")
    Q.set_left_child(P)
    Q.set_right_child(f)

    return Q

def b6():
    M = standard(3)

    P = Node(2, "P")
    P.black = True
    x = Node(1, 'x')
    x.black = True
    P.set_left_child(x)

    Q = Node(10, "Q")
    f = Node(11, 'f')
    f.black = True
    Q.set_right_child(f)
    Q.set_left_child(M)
    P.set_right_child(Q)

    return P

def print_rb(rb, filename):
    with open(filename, 'w') as of:
        of.write('digraph rb {\n')
        of.write('  node[shape = record];\n')
        out = rb.dot()
        of.write(out[0])
        of.write('}')

def insert():
    R = Node(60, 60)
    R.black = True
    R = R.insert(30, 30)
    R = R.insert(10, 10)
    R = R.insert(20, 20)
    R = R.insert(50, 50)
    R = R.insert(40, 40)
    R = R.insert(70, 70)
    R = R.insert(80, 80)
    R = R.insert(15, 15)
    R = R.insert(90, 90)
    R = R.insert(100, 100)

    print_rb(R, "R.dot")


#insert()

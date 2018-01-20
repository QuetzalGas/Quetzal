from random import shuffle
from itertools import permutations
from unittest import TestCase

from datastructures import *
from datastructures.adt_red_black_tree import Node

def check_preorder(insert_lst, order_lst, black_lst):
    if len(order_lst) != len(black_lst):
        return False

    a = adt_red_black_tree.AdtRedBlackTree()

    for i in insert_lst:
        a.insert(i)

    test_lst = list(a.iter_preorder())

    if len(test_lst) != len(order_lst):
        return False

    for (i, j, color) in zip(test_lst, order_lst, black_lst):
        print(i, j)
        if (i[0] != j) or (i[2] != color):
            return False

    return True

def print_tests():
    print(check_preorder([0, 1], [0, 1], [True, False]))
    print(check_preorder([1, 0], [1, 0], [True, False]))

    print(check_preorder([0, 1, 2, 3], [1, 0, 2, 3], [True, True, True, False]))
    print(check_preorder([0, 1, 3, 2], [1, 0, 3, 2], [True, True, True, False]))

    print(check_preorder([2, 4, 5, 1, 3], [4, 2, 1, 3, 5], [True, True, False, False, True]))
    print(check_preorder([2, 5, 6, 1, 4, 3], [5, 2, 1, 4, 3, 6], [True, False, True, True, False, True]))

def four_node_with_leaves(min_key = 0):
    a = Node(min_key + 0, 'a')
    a.black = True
    b = Node(min_key + 2, 'b')
    b.black = True
    c = Node(min_key + 4, 'c')
    c.black = True
    d = Node(min_key + 6, 'd')
    d.black = True

    S = Node(min_key + 1, 'S')
    S.set_left_child(a)
    S.set_right_child(b)

    L = Node(min_key + 5, 'L')
    L.set_left_child(c)
    L.set_right_child(d)

    M = Node(min_key + 3, 'M')
    M.black = True
    M.set_left_child(S)
    M.set_right_child(L)

    return M

def four_node_with_two_node_parent_a():
    """
           P
          / \ 
         M   e
        . .
       .   .
      S     L
     / \   / \ 
    a   b c   d
    """
    M = four_node_with_leaves()

    P = Node(7, 'P')
    P.black = True

    e = Node(8, 'e')
    e.black = True
    P.set_right_child(e)

    P.set_left_child(M)

    return P, M

def four_node_with_two_node_parent_b():
    """
       P
      / \ 
     e   M
        . .
       .   .
      S     L
     / \   / \ 
    a   b c   d
    """
    M = four_node_with_leaves(2)

    P = Node(1, 'P')
    P.black = True

    e = Node(0, 'e')
    e.black = True
    P.set_left_child(e)

    P.set_right_child(M)

    return P, M

    """
         M
        . .
       .   .
      S     L
     / \   / \ 
    a   b c   d
    """


def four_node_with_three_node_parent_a_right():
    """
             P
            / .
          /     .
         M       Q
        . .     / \ 
       .   .   e   f
      S     L
     / \   / \ 
    a   b c   d
    """
    M = four_node_with_leaves()

    P = Node(7, 'P')
    P.black = True
    P.set_left_child(M)

    Q = Node(9, 'Q')
    P.set_right_child(Q)

    e = Node(8, 'e')
    e.black = True
    f = Node(10, 'f')
    f.black = True

    Q.set_left_child(e)
    Q.set_right_child(f)

    return P, M

def four_node_with_three_node_parent_a_left():
    """
             Q
            . \ 
           P   f
          / \ 
         M   e
        . .
       .   .
      S     L
     / \   / \ 
    a   b c   d
    """
    M = four_node_with_leaves()

    P = Node(7, 'P')
    P.set_left_child(M)

    e = Node(8, 'e')
    e.black = True
    P.set_right_child(e)

    Q = Node(9, 'Q')
    Q.black = True
    Q.set_left_child(P)

    f = Node(10, 'f')
    f.black = True
    Q.set_right_child(f)

    return Q, M

def four_node_with_three_node_parent_b_right():
    """
         P
        / .
       e   Q
          / \ 
         M   f
        . .
       .   .
      S     L
     / \   / \ 
    a   b c   d
    """
    M = four_node_with_leaves(2)

    P = Node(1, 'P')
    P.black = True

    e = Node(0, 'e')
    e.black = True
    P.set_left_child(e)

    Q = Node(9, 'Q')
    P.set_right_child(Q)

    Q.set_left_child(M)

    f = Node(10, 'f')
    f.black = True
    Q.set_right_child(f)

    return P, M

def four_node_with_three_node_parent_b_left():
    """
         Q
        . \ 
       P   f
      / \ 
     e   M
        . .
       .   .
      S     L
     / \   / \ 
    a   b c   d
    """
    M = four_node_with_leaves(2)

    Q = Node(9, 'Q')
    Q.black = True

    f = Node(10, 'f')
    f.black = True
    Q.set_right_child(f)

    P = Node(1, 'P')
    Q.set_left_child(P)

    e = Node(0, 'e')
    e.black = True
    P.set_left_child(e)

    P.set_right_child(M)

    return Q, M

def four_node_with_three_node_parent_c_right():
    """
      P
     / . 
    e   Q
       / \ 
      f   M
         . .
        .   .
       S     L
      / \   / \ 
     a   b c   d
    """
    M = four_node_with_leaves(4)

    P = Node(1, 'P')
    P.black = True

    e = Node(0, 'e')
    e.black = True
    P.set_left_child(e)

    Q = Node(3, 'Q')
    P.set_right_child(Q)

    f = Node(2, 'f')
    f.black = True
    Q.set_left_child(f)

    Q.set_right_child(M)

    return P, M

def four_node_with_three_node_parent_c_left():
    """
          Q
         . \ 
       .     \ 
      P       M
     / \     . .
    e   f   .   .
           S     L
          / \   / \ 
         a   b c   d
    """
    M = four_node_with_leaves(4)

    Q = Node(3, 'Q')
    Q.black = True

    P = Node(1, 'P')
    Q.set_left_child(P)

    e = Node(0, 'e')
    e.black = True
    P.set_left_child(e)

    f = Node(2, 'f')
    f.black = True
    P.set_right_child(f)

    Q.set_right_child(M)

    return Q, M

def get_preorder_sequence_and_red_nodes(tree):
    keys = [x[0] for x in tree.iter_preorder()]
    red_nodes = [x[0] for x in tree.iter_preorder() if x[2] == False]

    return (keys, red_nodes)

class TestRbTree(TestCase):
    def test_four_node_preorder_sequence(self):
        rb = AdtRedBlackTree()
        rb.root = four_node_with_leaves()

        keys, red_nodes = get_preorder_sequence_and_red_nodes(rb)

        self.assertEqual(keys, [3, 1, 0, 2, 5, 4, 6])
        self.assertEqual(red_nodes, [1, 5])

    def test_insertion_3_fix(self):
        for i in permutations([0, 1, 2]):
            rb = AdtRedBlackTree()

            for j in i:
                rb.insert(j)

            keys, red_nodes = get_preorder_sequence_and_red_nodes(rb)

            self.assertEqual(keys, [1, 0, 2])
            self.assertEqual(red_nodes, [0, 2])

    def test_split_two_node_parent_a(self):
        pre_keys = [7, 3, 1, 0, 2, 5, 4, 6, 8]
        pre_red = [1, 5]
        post_keys = [7, 3, 1, 0, 2, 5, 4, 6, 8]
        post_red = [3]

        root, four_node = four_node_with_two_node_parent_a()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red)

    def test_split_two_node_parent_b(self):
        pre_keys = [1, 0, 5, 3, 2, 4, 7, 6, 8]
        pre_red = [3, 7]
        post_keys = [1, 0, 5, 3, 2, 4, 7, 6, 8]
        post_red = [5]

        root, four_node = four_node_with_two_node_parent_b()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red)

    def test_split_three_node_parent_a_right(self):
        pre_keys = [7, 3, 1, 0, 2, 5, 4, 6, 9, 8, 10]
        pre_red = [1, 5, 9]
        post_keys = [7, 3, 1, 0, 2, 5, 4, 6, 9, 8, 10]
        post_red = [3, 9]

        root, four_node = four_node_with_three_node_parent_a_right()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red)

    def test_split_three_node_parent_a_left(self):
        pre_keys = [9, 7, 3, 1, 0, 2, 5, 4, 6, 8, 10]
        pre_red = [7, 1, 5]
        post_keys = [7, 3, 1, 0, 2, 5, 4, 6, 9, 8, 10]
        post_red = [3, 9]

        root, four_node = four_node_with_three_node_parent_a_left()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red)

    def test_split_three_node_parent_b_right(self):
        pre_keys = [1, 0, 9, 5, 3, 2, 4, 7, 6, 8, 10]
        pre_red = [9, 3, 7]
        post_keys = [5, 1, 0, 3, 2, 4, 9, 7, 6, 8, 10]
        post_red = [1, 9]

        root, four_node = four_node_with_three_node_parent_b_right()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red)

    def test_split_three_node_parent_b_left(self):
        pre_keys = [9, 1, 0, 5, 3, 2, 4, 7, 6, 8, 10]
        pre_red = [1, 3, 7]
        post_keys = [5, 1, 0, 3, 2, 4, 9, 7, 6, 8, 10]
        post_red = [1, 9]

        root, four_node = four_node_with_three_node_parent_b_left()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red)

    def test_split_three_node_parent_c_right(self):
        pre_keys = [1, 0, 3, 2, 7, 5, 4, 6, 9, 8, 10]
        pre_red = [3, 5, 9]
        post_keys = [3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10] 
        post_red = [1, 7]

        root, four_node = four_node_with_three_node_parent_c_right()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red)

    def test_split_three_node_parent_c_left(self):
        pre_keys = [3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10]
        pre_red = [1, 5, 9]
        post_keys = [3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10]
        post_red = [1, 7]

        root, four_node = four_node_with_three_node_parent_c_left()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red)

    def pre_post_split(self, four_node, pre_keys, pre_red, post_keys, post_red):
        rb = AdtRedBlackTree()
        rb.root = four_node.find_root()

        keys, red_nodes = get_preorder_sequence_and_red_nodes(rb)

        self.assertEqual(keys, pre_keys)
        self.assertEqual(red_nodes, pre_red)

        four_node.split()

        rb.root = four_node.find_root()

        keys, red_nodes = get_preorder_sequence_and_red_nodes(rb)

        self.assertEqual(keys, post_keys)
        self.assertEqual(red_nodes, post_red)

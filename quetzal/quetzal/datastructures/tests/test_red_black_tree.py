from random import shuffle
from itertools import permutations
from unittest import TestCase

import os
import shutil

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

def two_node_with_leaves(min_key = 0, value = 'P', leaves = ['a', 'b']):
    """
      P
     / \ 
    a   b
    """
    a = Node(min_key + 0, leaves[0])
    a.black = True

    b = Node(min_key + 2, leaves[1])
    b.black = True

    P = Node(min_key + 1, value)
    P.black = True

    P.set_left_child(a)
    P.set_right_child(b)

    return P

def four_node_with_leaves(min_key = 0, values = ['S', 'M', 'L'], leaves = ['a', 'b', 'c', 'd']):
    """
         M
        . .
       .   .
      S     L
     / \   / \ 
    a   b c   d
    """
    S = two_node_with_leaves(min_key, 'S', leaves[0:2])
    S.black = False

    L = two_node_with_leaves(min_key + 4, 'L', leaves[2:4])
    L.black = False

    M = Node(min_key + 3, values[1])
    M.black = True
    M.set_left_child(S)
    M.set_right_child(L)

    return M

def three_node_left_with_leaves(min_key = 0, values = ['S', 'L'], leaves = ['a', 'b', 'c']):
    """
        L
       . \ 
      S   c
     / \ 
    a   b
    """
    S = two_node_with_leaves(min_key, values[0], leaves[0:2])
    S.black = False
    pass

def three_node_right_with_leaves(min_key = 0, values = ['S', 'L'], leaves = ['a', 'b', 'c']):
    """
      S
     / .
    a   L
       / \ 
      b   c
    """
    pass

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

    return M

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

    return M

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

    return M

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

    return M

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

    return M

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

    return M

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

    return M

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

    return M

def two_node_with_two_parent():
    pass

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
                rb[j] = j

            keys, red_nodes = get_preorder_sequence_and_red_nodes(rb)

            self.assertEqual(keys, [1, 0, 2])
            self.assertEqual(red_nodes, [0, 2])

    def test_split_two_node_parent_a(self):
        pre_keys = [7, 3, 1, 0, 2, 5, 4, 6, 8]
        pre_red = [1, 5]
        post_keys = [7, 3, 1, 0, 2, 5, 4, 6, 8]
        post_red = [3]

        four_node = four_node_with_two_node_parent_a()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red, 'split_two_a')

    def test_split_two_node_parent_b(self):
        pre_keys = [1, 0, 5, 3, 2, 4, 7, 6, 8]
        pre_red = [3, 7]
        post_keys = [1, 0, 5, 3, 2, 4, 7, 6, 8]
        post_red = [5]

        four_node = four_node_with_two_node_parent_b()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red, 'split_two_b')

    def test_split_three_node_parent_a_right(self):
        pre_keys = [7, 3, 1, 0, 2, 5, 4, 6, 9, 8, 10]
        pre_red = [1, 5, 9]
        post_keys = [7, 3, 1, 0, 2, 5, 4, 6, 9, 8, 10]
        post_red = [3, 9]

        four_node = four_node_with_three_node_parent_a_right()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red, 'split_three_a_right')

    def test_split_three_node_parent_a_left(self):
        pre_keys = [9, 7, 3, 1, 0, 2, 5, 4, 6, 8, 10]
        pre_red = [7, 1, 5]
        post_keys = [7, 3, 1, 0, 2, 5, 4, 6, 9, 8, 10]
        post_red = [3, 9]

        four_node = four_node_with_three_node_parent_a_left()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red, 'split_three_a_left')

    def test_split_three_node_parent_b_right(self):
        pre_keys = [1, 0, 9, 5, 3, 2, 4, 7, 6, 8, 10]
        pre_red = [9, 3, 7]
        post_keys = [5, 1, 0, 3, 2, 4, 9, 7, 6, 8, 10]
        post_red = [1, 9]

        four_node = four_node_with_three_node_parent_b_right()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red, 'split_three_b_right')

    def test_split_three_node_parent_b_left(self):
        pre_keys = [9, 1, 0, 5, 3, 2, 4, 7, 6, 8, 10]
        pre_red = [1, 3, 7]
        post_keys = [5, 1, 0, 3, 2, 4, 9, 7, 6, 8, 10]
        post_red = [1, 9]

        four_node = four_node_with_three_node_parent_b_left()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red, 'split_three_b_left')

    def test_split_three_node_parent_c_right(self):
        pre_keys = [1, 0, 3, 2, 7, 5, 4, 6, 9, 8, 10]
        pre_red = [3, 5, 9]
        post_keys = [3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10] 
        post_red = [1, 7]

        four_node = four_node_with_three_node_parent_c_right()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red, 'split_three_c_right')

    def test_split_three_node_parent_c_left(self):
        pre_keys = [3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10]
        pre_red = [1, 5, 9]
        post_keys = [3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10]
        post_red = [1, 7]

        four_node = four_node_with_three_node_parent_c_left()
        self.pre_post_split(four_node, pre_keys, pre_red, post_keys, post_red, 'split_three_c_left')

    def test_combine_2p_2s(self):
        for i in [1, 5]:
            rb = AdtRedBlackTree()
            rb.from_deser([3, 1, 0, 2, 5, 4, 6], [])

            rb.root[i].combine()
            rb.root = rb.root.find_root()

            keys, red = get_preorder_sequence_and_red_nodes(rb)

            self.assertEqual(keys, [3, 1, 0, 2, 5, 4, 6])
            self.assertEqual(red, [1, 5])

    def test_combine_2p_3s(self):
        rb = AdtRedBlackTree()

        #       3
        #     /   \ 
        #   1       5
        #  / \     / .
        # 0   2   4   7
        #            / \ 
        #           6   8
        left_right_leaning = [3, 1, 0, 2, 5, 4, 7, 6, 8]
        rb.from_deser(left_right_leaning, [7])

        rb.root[1].combine()
        rb.root = rb.root.find_root()

        keys, red = get_preorder_sequence_and_red_nodes(rb)
                
        #         5
        #       /   \
        #     3       7
        #    . \     / \
        #   1   4   6   8
        #  / \
        # 0   2
        self.assertEqual(keys, [5, 3, 1, 0, 2, 4, 7, 6, 8])
        self.assertEqual(red, [1])

        rb.root[7].combine()
        rb.root = rb.root.find_root()

        keys, red = get_preorder_sequence_and_red_nodes(rb)

        self.assertEqual(keys, left_right_leaning)
        self.assertEqual(red, [7])

        #       3
        #     /   \
        #   1       7
        #  / \     . \
        # 0   2   5   8
        #        / \
        #       4   6
        rb.from_deser([3, 1, 0, 2, 7, 5, 4, 6, 8], [5])

        rb.root[1].combine()
        rb.root = rb.root.find_root()

        keys, red = get_preorder_sequence_and_red_nodes(rb)
        self.assertEqual(keys, [5, 3, 1, 0, 2, 4, 7, 6, 8])
        self.assertEqual(red, [1])

    def test_combine_2p_x1(self):
        # right sibling is 4 node.
        pre = [3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10]
        pre_red = [5, 9]

        expected = [5, 3, 1, 0, 2, 4, 7, 6, 9, 8, 10]
        expected_red = [1, 9]

        self.pre_post_combine(1, pre, pre_red, expected, expected_red, 'combine_2p_x1')

    def test_combine_2p_x(self):
        # left sibling is 4 node.
        pre = [7, 3, 1, 0, 2, 5, 4, 6, 9, 8, 10]
        pre_red = [1, 5]

        expected = [5, 3, 1, 0, 2, 4, 7, 6, 9, 8, 10]
        expected_red = [1, 9]

        self.pre_post_combine(9, pre, pre_red, expected, expected_red, 'combine_2p_x')

    def test_combine_3p_merge(self):
        case_1 = [7, 3, 1, 0, 2, 5, 4, 6, 9, 8, 10]
        case_1_red = [3]

        case_2 = [3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10]
        case_2_red = [7]

        self.pre_post_combine(1, case_1, case_1_red, case_1, [1, 5], 'combine_3p_merge_1')
        self.pre_post_combine(1, case_2, case_2_red, case_1, [1, 5], 'combine_3p_merge_2')

        self.pre_post_combine(5, case_1, case_1_red, case_1, [1, 5], 'combine_3p_merge_3')
        self.pre_post_combine(5, case_2, case_2_red, case_1, [1, 5], 'combine_3p_merge_4')
        
        self.pre_post_combine(9, case_1, case_1_red, case_2, [5, 9], 'combine_3p_merge_5')
        self.pre_post_combine(9, case_2, case_2_red, case_2, [5, 9], 'combine_3p_merge_6')

    def test_combine_3p_1(self):
        case_1 = [7, 1, 0, 3, 2, 5, 4, 6, 9, 8, 10]
        case_1_red = [1, 5]

        case_2 = [1, 0, 7, 3, 2, 5, 4, 6, 9, 8, 10]
        case_2_red = [7, 5]

        case_3 = [7, 1, 0, 5, 3, 2, 4, 6, 9, 8, 10]
        case_3_red = [1, 3]

        case_4 = [1, 0, 7, 5, 3, 2, 4, 6, 9, 8, 10]
        case_4_red = [7, 3]

        expected = [5, 1, 0, 3, 2, 4, 7, 6, 9, 8, 10]
        expected_red = [1, 9]

        self.pre_post_combine(9, case_1, case_1_red, expected, expected_red, 'combine_3p_1_1')
        self.pre_post_combine(9, case_2, case_2_red, expected, expected_red, 'combine_3p_1_2')
        self.pre_post_combine(9, case_3, case_3_red, expected, expected_red, 'combine_3p_1_3')
        self.pre_post_combine(9, case_4, case_4_red, expected, expected_red, 'combine_3p_1_4')

    def test_combine_3p_2(self):
        case_1 = [1, 0, 9, 5, 3, 2, 4, 7, 6, 8, 11, 10, 12]
        case_1_red = [9, 3, 7]

        case_2 = [9, 1, 0, 5, 3, 2, 4, 7, 6, 8, 11, 10, 12]
        case_2_red = [1, 3, 7]

        expected = [7, 1, 0, 5, 3, 2, 4, 6, 9, 8, 11, 10, 12]
        expected_red = [1, 3, 11]

        self.pre_post_combine(11, case_1, case_1_red, expected, expected_red, 'combine_3p_2_1')
        self.pre_post_combine(11, case_2, case_2_red, expected, expected_red, 'combine_3p_2_2')

    def test_combine_3p_3(self):
        case_1 = [5, 1, 0, 3, 2, 4, 9, 7, 6, 8, 10]
        case_1_red = [3, 9]

        case_2 = [5, 3, 1, 0, 2, 4, 9, 7, 6, 8, 10]
        case_2_red = [1, 9]

        case_3 = [9, 5, 1, 0, 3, 2, 4, 7, 6, 8, 10]
        case_3_red = [5, 3]

        case_4 = [9, 5, 3, 1, 0, 2, 4, 7, 6, 8, 10]
        case_4_red = [5, 1]

        expected = [3, 1, 0, 2, 9, 5, 4, 7, 6, 8, 10]
        expected_red = [9, 7]

        self.pre_post_combine(7, case_1, case_1_red, expected, expected_red, 'combine_3p_3_1')
        self.pre_post_combine(7, case_2, case_2_red, expected, expected_red, 'combine_3p_3_2')
        self.pre_post_combine(7, case_3, case_3_red, expected, expected_red, 'combine_3p_3_3')
        self.pre_post_combine(7, case_4, case_4_red, expected, expected_red, 'combine_3p_3_4')

    def test_combine_3p_4(self):
        case_1 = [11, 7,3, 1, 0, 2, 5, 4, 6, 9, 8, 10, 12]
        case_1_red = [7, 1, 5]

        case_2 = [7, 3, 1, 0, 2, 5, 4, 6, 11, 9, 8, 10, 12]
        case_2_red = [1, 5, 11]

        expected = [5, 3, 1, 0, 2, 4, 11, 7, 6, 9,8, 10, 12]
        expected_red = [1, 11, 9]

        self.pre_post_combine(9, case_1, case_1_red, expected, expected_red, 'combine_3p_4_1')
        self.pre_post_combine(9, case_2, case_2_red, expected, expected_red, 'combine_3p_4_2')

    def test_combine_3p_5(self):
        case_1 = [9, 3, 1, 0, 2, 5, 4, 7, 6, 8, 10]
        case_1_red = [3, 7]

        case_2 = [9, 3, 1, 0, 2, 7, 5, 4, 6, 8, 10]
        case_2_red = [3, 5]

        case_3 = [3, 1, 0, 2, 9, 5, 4, 7, 6, 8, 10]
        case_3_red = [9, 7]

        case_4 = [3, 1, 0, 2, 9, 7, 5, 4, 6, 8, 10]
        case_4_red = [9, 5]

        expected = [5, 3, 1, 0, 2, 4, 9, 7, 6, 8, 10]
        expected_red = [1, 9]

        self.pre_post_combine(1, case_1, case_1_red, expected, expected_red, 'combine_3p_5_1')
        self.pre_post_combine(1, case_2, case_2_red, expected, expected_red, 'combine_3p_5_2')
        self.pre_post_combine(1, case_3, case_3_red, expected, expected_red, 'combine_3p_5_3')
        self.pre_post_combine(1, case_4, case_4_red, expected, expected_red, 'combine_3p_5_4')

    def test_combine_3p_6(self):
        case_1 = [11, 3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10, 12]
        case_1_red = [3, 5, 9]

        case_2 = [3, 1, 0, 2, 11, 7, 5, 4, 6, 9, 8, 10, 12]
        case_2_red = [11, 5, 9]

        expected = [5, 3, 1, 0, 2, 4, 11, 7, 6, 9, 8, 10, 12]
        expected_red = [1, 11, 9]

        self.pre_post_combine(1, case_1, case_1_red, expected, expected_red, 'combine_3p_6_1')
        self.pre_post_combine(1, case_2, case_2_red, expected, expected_red, 'combine_3p_6_2')

    def test_combine_4p_1(self):
        case_1 = [3, 1, 0, 2, 9, 7, 5, 4, 6, 8, 11, 10, 12]
        case_1_red = [1, 9, 5]

        case_2 = [3, 1, 0, 2, 9, 5, 4, 7, 6, 8, 11, 10, 12]
        case_2_red = [1, 9, 7]

        expected = [3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 11, 10, 12]
        expected_red = [1, 7, 11]

        self.pre_post_combine(11, case_1, case_1_red, expected, expected_red, 'combine_4p_1_1')
        self.pre_post_combine(11, case_2, case_2_red, expected, expected_red, 'combine_4p_1_2')

    def test_combine_4p_2(self):
        pre = [3, 1, 0, 2, 11, 7, 5, 4, 6, 9, 8, 10, 13, 12, 14]
        pre_red = [1, 11, 5, 9]

        expected = [3, 1, 0, 2, 9, 7, 5, 4, 6, 8, 11, 10, 13, 12, 14]
        expected_red = [1, 9, 5, 13]

        self.pre_post_combine(13, pre, pre_red, expected, expected_red, 'combine_4p_2')

    def test_combine_4p_3(self):
        case_1 = [7, 1, 0, 5, 3, 2, 4, 6, 11, 9, 8, 10, 12]
        case_1_red = [1, 3, 11]

        case_2 = [7, 1, 0, 3, 2, 5, 4, 6, 11, 9, 8, 10, 12]
        case_2_red = [1, 5, 11]

        expected = [5, 1, 0, 3, 2, 4, 11, 9, 7, 6, 8, 10, 12]
        expected_red = [1, 11, 7]

        self.pre_post_combine(9, case_1, case_1_red, expected, expected_red, 'combine_4p_3_1')
        self.pre_post_combine(9, case_2, case_2_red, expected, expected_red, 'combine_4p_3_2')

    def test_combine_4p_4(self):
        pre = [9, 1, 0, 5, 3, 2,4, 7, 6, 8, 13, 11, 10, 12, 14]
        pre_red = [1, 3, 7, 13]

        expected = [7, 1, 0, 5, 3, 2, 4, 6, 13, 11, 9,8, 10, 12, 14]
        expected_red = [1, 3, 13, 9]

        self.pre_post_combine(11, pre, pre_red, expected, expected_red, 'combine_4p_4')

    def test_combine_4p_5(self):
        case_a = [9, 5, 3, 1, 0, 2, 4, 7, 6, 8, 11, 10, 12]
        case_a_red = [5, 1, 11]

        case_b = [9, 5, 1, 0, 3, 2, 4, 7, 6, 8, 11, 10, 12]
        case_b_red = [5, 3, 11]

        expected = [9, 3, 1, 0, 2, 5, 4, 7, 6, 8, 11, 10, 12]
        expected_red = [3, 7, 11]

        self.pre_post_combine(7, case_a, case_a_red, expected, expected_red, 'combine_4p_5a')
        self.pre_post_combine(7, case_b, case_b_red, expected, expected_red, 'combine_4p_5b')

    def test_combine_4p_6(self):
        pre = [11, 7, 3, 1, 0, 2, 5, 4, 6, 9, 8, 10, 13, 12, 14]
        pre_red = [7, 1, 5, 13]

        expected = [11, 5, 3, 1, 0, 2, 4, 7, 6, 9, 8, 10, 13, 12, 14]
        expected_red = [5, 1, 9,13]

        self.pre_post_combine(9, pre, pre_red, expected, expected_red, 'combine_4p_6')

    def test_combine_4p_7(self):
        case_a = [9, 3, 1, 0, 2, 5, 4, 7, 6, 8, 11, 10, 12]
        case_a_red = [3, 7, 11]

        case_b = [9, 3, 1, 0, 2, 7, 5, 4, 6, 8, 11, 10, 12]
        case_b_red = [3, 5, 11]

        expected = [9, 5, 3, 1, 0, 2, 4, 7, 6, 8, 11, 10, 12]
        expected_red = [5, 1, 11]

        self.pre_post_combine(1, case_a, case_a_red, expected, expected_red, 'combine_4p_7a')
        self.pre_post_combine(1, case_b, case_b_red, expected, expected_red, 'combine_4p_7b')

    def test_combine_4p_8(self):
        pre = [11, 3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10, 13, 12, 14]
        pre_red = [3, 5, 9, 13]

        expected = [11, 5, 3, 1, 0, 2, 4, 7, 6, 9, 8, 10, 13, 12, 14]
        expected_red = [5, 1, 9, 13]

        self.pre_post_combine(1, pre, pre_red, expected, expected_red, 'combine_4p_8')

    def test_combine_4p_m1(self):
        pre = [3, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10]
        pre_red = [1, 7]

        expected = pre
        expected_red = [1, 5, 9]

        self.pre_post_combine(9, pre, pre_red, expected, expected_red, 'combine_4p_m1')

    def test_combine_4p_m2(self):
        pre = [5, 1, 0, 3, 2, 4, 9, 7,6, 8, 10]
        pre_red = [1, 9]

        expected = [1, 0, 9, 5, 3, 2, 4, 7, 6, 8, 10]
        expected_red = [9, 3, 7]

        self.pre_post_combine(7, pre, pre_red, expected, expected_red, 'combine_4p_m2')

    def test_combine_4p_m3(self):
        pre = [7, 3, 1, 0, 2, 5, 4, 6, 9, 8, 10]
        pre_red = [3, 9]

        expected = pre
        expected_red = [1, 5, 9]

        self.pre_post_combine(5, pre, pre_red, expected, expected_red, 'combine_4p_m3')

    def test_combine_4p_m4(self):
        pre = [7, 3, 1, 0, 2, 5, 4, 6, 9, 8, 10]
        pre_red = [3, 9]

        expected = pre
        expected_red = [1, 5, 9]

        self.pre_post_combine(1, pre, pre_red, expected, expected_red, 'combine_4p_m4')

    def pre_post_combine(self, two_node, pre_keys, pre_red, post_keys, post_red, name):
        rb = AdtRedBlackTree()
        rb.from_deser(pre_keys, pre_red)

        self.create_directory(name)
        self.write_dot_and_execute(rb, '{}/pre'.format(name))

        keys, red = get_preorder_sequence_and_red_nodes(rb)

        self.assertEqual(keys, pre_keys)
        self.assertEqual(red, pre_red)

        two_node = rb.root[two_node]
        two_node.combine()
        rb.root = two_node.find_root()

        self.write_dot_and_execute(rb, name + '/post')

        keys, red = get_preorder_sequence_and_red_nodes(rb)

        self.assertEqual(keys, post_keys)
        self.assertEqual(red, post_red)

    def pre_post_split(self, four_node, pre_keys, pre_red, post_keys, post_red, l = 'temp'):
        rb = AdtRedBlackTree()
        rb.root = four_node.find_root()

        self.create_directory(l)
        self.write_dot_and_execute(rb, '{}/pre'.format(l))

        keys, red_nodes = get_preorder_sequence_and_red_nodes(rb)

        self.assertEqual(keys, pre_keys)
        self.assertEqual(red_nodes, pre_red)

        four_node.split()
        rb.root = four_node.find_root()

        self.write_dot_and_execute(rb, l + '/post')

        keys, red_nodes = get_preorder_sequence_and_red_nodes(rb)

        self.assertEqual(keys, post_keys)
        self.assertEqual(red_nodes, post_red)

    def write_dot_and_execute(self, rb, filename):
        self.write_file(rb, filename + '.dot')

        directory = 'tests/test_output/red_black_tree'
        filename = directory + '/' + filename
        os.system('dot -Tpng {} -o {}'.format(filename + '.dot', filename + '.png'))

    def write_file(self, rb, filename):
        directory = 'tests/test_output/red_black_tree'

        with open(directory + '/' + filename, 'w') as of:
            of.write('digraph rb {\n')
            of.write('  node[shape = record];\n')
            out = rb.__repr__()
            of.write(out[0])
            of.write('  labelloc="t";\n')
            of.write('  label="{}";\n'.format('dd'))
            of.write('}')

    def create_directory(self, directory):
        root = 'tests/test_output/red_black_tree'
        if not os.path.exists(root + '/' + directory):
            os.makedirs(root + '/' + directory)

    @classmethod
    def setUpClass(cls):
        root = 'tests/test_output/red_black_tree'

        if os.path.exists(root):
            shutil.rmtree(root)

        if not os.path.exists(root):
            os.makedirs(root)

    def test_deser(self):
        for i in range(0, 20):
            rb = AdtRedBlackTree()

            deserialize_keys = [x for x in range(1, 10)]
            shuffle(deserialize_keys)

            rb.from_deser(deserialize_keys, [])

            keys, red_nodes = get_preorder_sequence_and_red_nodes(rb)

            self.assertEqual(deserialize_keys, keys)

from random import shuffle
from itertools import permutations
from unittest import TestCase

from datastructures import *
from datastructures.adt_red_black_tree import Node

def rnd():
    a = AdtRedBlackTree()

    x = [i for i in range(0, 10)]
    shuffle(x)

    for i in x:
        a.insert(i)

    for i in a.iter_preorder():
        print(i)


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

def check_3_insert():
    for i in permutations([0, 1, 2]):
        if not check_preorder(i, [1, 0, 2], [True, False, False]):
            return False

    return True

def print_tests():
    print(check_preorder([0, 1], [0, 1], [True, False]))
    print(check_preorder([1, 0], [1, 0], [True, False]))

    print('Check 3 insert:', check_3_insert())

    print(check_preorder([0, 1, 2, 3], [1, 0, 2, 3], [True, True, True, False]))
    print(check_preorder([0, 1, 3, 2], [1, 0, 3, 2], [True, True, True, False]))

    print(check_preorder([2, 4, 5, 1, 3], [4, 2, 1, 3, 5], [True, True, False, False, True]))
    print(check_preorder([2, 5, 6, 1, 4, 3], [5, 2, 1, 4, 3, 6], [True, False, True, True, False, True]))

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

def validate_preorder_sequence(tree, key_lst, red_map):
    tree_lst = list(tree.iter_preorder())

    if len(tree_lst) != len(key_lst):
        return False

    for (tree_item, key) in zip(tree_lst, key_lst):
        if tree_item[0] != key:
            return False

        if tree_item[2]:
            if tree_item[0] in red_map:
                return False
        else:
            if tree_item[0] not in red_map:
                return False

    print("SUCCES")
    return True

class TestRbTree(TestCase):
    def test_1(self):
        rb = AdtRedBlackTree()
        rb.root = standard()

        rb.dot('k.dot', 'label')
        dot_text = rb.__repr__()

        for i in rb.iter_preorder():
            print(i)

        k = validate_preorder_sequence(rb, [3, 1, 0, 2, 5, 4, 6], [1, 5])

        self.assertTrue(k)

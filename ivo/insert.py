#! /bin/python3

from rb_tree import RbTree

def case_a():
    tree = RbTree()

    tree.insert(2, 'M')
    tree.insert(1, 'S')
    tree.insert(3, 'L')
    tree.root.add_dummy_leaves('a')
    tree.dot('case_a.dot', 'case_a')

case_a()

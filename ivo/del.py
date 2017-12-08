#! /bin/python3
from rb_tree import RbTree

def output(name, values):
    a = RbTree()
    iorder = ''

    for v in values:
        a.insert(v)
        iorder += '_{}'.format(v)
        a.dot(name + iorder + '.dot', 'insert order: ' + iorder)

    a.dot(name, iorder)

output('dump/rb_2_2_1_v1', [1, 5, 6, 2, 4, 3])
output('dump/rb_2_2_1_v2', [1, 5, 6, 2, 3, 4])
output('dump/rb_2_2_1_v3', [1, 2, 6, 5, 4, 3])
output('dump/rb_2_2_1_v4', [1, 2, 6, 5, 3, 4])

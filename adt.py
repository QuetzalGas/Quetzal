#! /usr/bin/python3

import sys
import os
import shutil
from quetzal.quetzal.datastructures import *

if len(sys.argv) != 2:
    print('Usage: ./adt.py adt.txt')
    exit()

# Clear previous output
if os.path.exists('adt-output'):
    shutil.rmtree('adt-output')

os.makedirs('adt-output')

current_adt = None
output_counter = 1

with open(sys.argv[1]) as commands:
    for line in commands:
        line = line.strip()

        if line.startswith('#'):
            continue

        if line.startswith('type='):
            line = line[5:]

            current_adt = None

            if line == 'bst':
                current_adt = AdtBinarySearchTree()
            elif line == 'stack':
                current_adt = AdtStack()
            elif line == 'queue':
                current_adt = AdtQueue()
            elif line == 'dll':
                current_adt = AdtDoublyLinkedList()
            elif line == 'cll':
                current_adt = AdtCircularLinkedList()
            elif line == '23':
                current_adt = AdtTwoThreeTree()
            elif line == '234':
                current_adt = AdtTwoThreeFourTree()
            elif line == 'rb':
                current_adt = AdtRedBlackTree()
            elif line == 'hlin':
                current_adt = AdtHashMap()
            elif line == 'hquad':
                current_adt = AdtHashMap()
            elif line == 'hsep':
                current_adt = AdtHashMap()
            else:
                print('Unknown type:', line)
                exit()

            output_counter = 1

        if current_adt is not None and line.startswith('insert '):
            line = line[7:]

            value = int(line)

            if isinstance(current_adt, AdtStack):
                current_adt.push(value)
            elif isinstance(current_adt, AdtQueue):
                current_adt.enqueue(value)
            elif isinstance(current_adt, (AdtDoublyLinkedList, AdtCircularLinkedList)):
                current_adt[0] = value
            elif isinstance(current_adt, (AdtBinarySearchTree, AdtTwoThreeTree, AdtTwoThreeFourTree, AdtRedBlackTree, AdtHashMap)):
                current_adt[value] = value
            else:
                print('Unknown error', current_adt)
                exit()

        if current_adt is not None and line.startswith('delete'):
            if isinstance(current_adt, AdtStack):
                current_adt.pop()
            elif isinstance(current_adt, AdtQueue):
                current_adt.dequeue()
            else:
                line = line[7:]

                del current_adt[int(line)]

        if current_adt is not None and line == 'print':
            if isinstance(current_adt, AdtBinarySearchTree):
                name = 'bst'
            elif isinstance(current_adt, AdtStack):
                name = 'stack'
            elif isinstance(current_adt, AdtQueue):
                name = 'queue'
            elif isinstance(current_adt, AdtDoublyLinkedList):
                name = 'dll'
            elif isinstance(current_adt, AdtCircularLinkedList):
                name = 'cll'
            elif isinstance(current_adt, AdtTwoThreeTree):
                name = '23'
            elif isinstance(current_adt, AdtTwoThreeFourTree):
                name = '234'
            elif isinstance(current_adt, AdtRedBlackTree):
                name = 'rb'
            elif isinstance(current_adt, AdtHashMap):
                name = 'hlin'
            else:
                print('No ADT to print')
                exit()

            full_name = 'adt-output/{}-{}'.format(name, output_counter)
            output_counter += 1

            with open(full_name + '.dot', 'w') as output:
                output.write(repr(current_adt))

            os.system('dot -Tpng {}.dot -o {}.png'.format(full_name, full_name))

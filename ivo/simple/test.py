#! /bin/python3

from adt_queue import Queue
from adt_doubly_linked_list import DoublyLinkedList
from adt_binary_search_tree import BinarySearchTree

with open('adt.txt') as f:
    adt = None
    counter = 1
    
    for line in f:
        line = line.strip()
        eq_split = line.split('=')
        sp_split = line.split(' ')

        if len(eq_split) == 2:
            if eq_split[0] == 'type':
                typ = eq_split[1]

                if typ == 'll':
                    adt = DoublyLinkedList()
                elif typ == 'queue':
                    adt = Queue()
                elif typ == 'bst':
                    adt = BinarySearchTree()
                else:
                    exit()
                counter = 1
        elif isinstance(adt, DoublyLinkedList):
            cmd = sp_split[0]

            if cmd == 'push_front':
                adt.push_front(int(sp_split[1]))
            elif cmd == 'push_back':
                adt.push_back(int(sp_split[1]))
            elif cmd == 'print':
                filename = 'll-{}.dot'.format(counter)
                adt.print(filename)
                counter += 1

        elif isinstance(adt, Queue):
            cmd = sp_split[0]

            if cmd == 'enqueue':
                adt.enqueue(int(sp_split[1]))
            elif cmd == 'dequeue':
                adt.dequeue()
            elif cmd == 'print':
                filename = 'queue-{}.dot'.format(counter)
                # Dit is voldoende om de correctheid te toetsen...
                adt.storage.print(filename)
                counter += 1
        elif isinstance(adt, BinarySearchTree):
            cmd = sp_split[0]

            if cmd == 'insert':
                val = int(sp_split[1])
                adt.insert(val, val)
            elif cmd == 'print':
                with open('bst-{}.dot'.format(counter), 'w') as of:
                    of.write('digraph bst {\n')
                    out = adt.dot()
                    of.write(out)
                    of.write('}')

                counter += 1

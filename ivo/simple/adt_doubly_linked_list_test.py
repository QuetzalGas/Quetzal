#! /bin/python3

from doubly_linked_list import DoublyLinkedList

with open('doubly_linked_chain.txt') as f:
    linked_list = None
    counter = 1

    for line in f:
        line = line.strip()
        eq_split = line.split('=')
        sp_split = line.split(' ')

        if len(eq_split) == 2:
            if eq_split[0] == 'type' and eq_split[1] == 'll':
                linked_list = DoublyLinkedList()
        elif linked_list is not None:
            if sp_split[0] == 'push_front':
                linked_list.push_front(int(sp_split[1]))
            elif sp_split[0] == 'push_back':
                linked_list.push_back(int(sp_split[1]))
            elif sp_split[0] == 'print':
                linked_list.print()
                counter += 1

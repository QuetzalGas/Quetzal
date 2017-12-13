#! /bin/python3

from adt_binary_search_tree import BinarySearchTree

with open('bst.txt') as f:
    bst = None
    counter = 1

    for line in f:
        line  = line.strip()
        eq_split = line.split('=')
        sp_split = line.split(' ')

        if len(eq_split) == 2:
            if eq_split[0] == 'type' and eq_split[1] == 'bst':
                bst = BinarySearchTree()
        elif bst is not None:
            if sp_split[0] == 'insert':
                v = int(sp_split[1])
                bst.insert(v, v)
            if sp_split[0] == 'delete':
                bst.delete(v, v)
            elif sp_split[0] == 'print':
                # Ik heb geen oplossing om de bst te tekenen, zonder de ADT
                # muur te doorbreken...
                with open('bst-{}.dot'.format(counter), 'w') as of:
                    of.write('digraph bst {\n')
                    out = bst.dot()
                    of.write(out)
                    of.write('}')

                counter += 1

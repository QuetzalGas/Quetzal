#! /bin/python3
class Node:
    def __init__(self, prev_node, next_node, item):
        self.prev_node = prev_node
        self.next_node = next_node
        self.item = item

    def insert_after(self, item):
        node = Node(self, self.next_node, item)
        self.next_node.prev_node = node
        self.next_node = node

    def insert_before(self, item):
        node = Node(self.prev_node, self, item)
        self.prev_node.next_node = node
        self.prev_node = node

    def remove(self):
        self.next_node.prev_node = self.prev_node
        self.prev_node.next_node = self.next_node
        return self.item

    def __iter__(self):
        ForwardIterator(self)

    def forward(self):
        ForwardIterator(self)

    def backward(self):
        BackwardIterator(self)


class Dummy(Node):
    def __init__(self, name):
        Node.__init__(self, self, self, name)


class BackwardIterator:
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        if not isinstance(self.current, Dummy):
            item = self.current.item
            self.current = self.current.prev_node
            return item
        else:
            raise StopIteration()


class ForwardIterator:
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        if not isinstance(self.current, Dummy):
            item = self.current.item
            self.current = self.current.next_node
            return item
        else:
            raise StopIteration()


class DoublyLinkedList:
    def __init__(self):
        self.dummy_head = Dummy('dummy_head')
        self.dummy_tail = Dummy('dummy_tail')
        self.dummy_head.next_node = self.dummy_tail
        self.dummy_tail.prev_node = self.dummy_head

    def get_length(self):
        length = 0

        for i in self:
            length +=1

        return length

    def push_front(self, item):
        self.dummy_head.insert_after(item)

    def front(self):
        if isinstance(self.dummy_head.next_node, Dummy):
            return None
        else:
            return self.dummy_head.next_node

    def push_back(self, item):
        self.dummy_tail.insert_before(item)

    def back(self):
        if isinstance(self.dummy_tail.prev_node, Dummy):
            return None
        else:
            return self.dummy_tail.prev_node

    def insert(self, index, item):
        pass

    def remove(self, index):
        pass

    def __iter__(self):
        return ForwardIterator(self.dummy_head.next_node)

    def back(self):
        return BackwardIterator(self.dummy_tail.prev_node)

    def print(self, filename):
        with open(filename, 'w') as f:
            f.write('digraph list {\n')
            f.write('  rankdir=LR;\n')
            f.write('  node [shape=record];\n')

            current = self.dummy_head

            while True:
                f.write('  {}->{}\n'.format(current.item, current.next_node.item))
                f.write('  {}->{}\n'.format(current.item, current.prev_node.item))
                if current == current.next_node:
                    break

                current = current.next_node

            f.write('}')

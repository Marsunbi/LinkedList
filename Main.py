#!/bin/python

class LinkedList(object):
    class Node(object):
        prev = None
        next = None

        def __init__(self, value):
            self.value = value

    first = None

    def add(self, value):
        if self.first is None:
            node = self.Node(value)
            self.first = node
        else:
            tmp = self.first
            while tmp.next is not None:
                tmp = tmp.next
            node = self.Node(value)
            tmp.next = node
            node.prev = tmp

    def get(self, index):
        if self.first is None:
            return None
        tmp = self.first
        i = 0
        while i < index:
            tmp = tmp.next
            i += 1
            if tmp.next is None:
                raise IndexError('Index out of bound at index {}'.format(index))
        return tmp.value

    def remove(self, value):
        if self.first is None:
            return None
        tmp = self.first
        while tmp is not None:
            if tmp.value is value:
                next = tmp.next
                prev = tmp.prev
                if next is not None:
                    next.prev = prev
                if prev is not None:
                    prev.next = next
                return tmp.value
            tmp = tmp.next
        return False

    def remove_at(self, index):
        if self.first is None:
            return None
        tmp = self.first
        i = 0
        while i < index:
            tmp = tmp.next
            i += 1
        prev = tmp.prev
        next = tmp.next
        prev.next = next
        if next is not None: next.prev = prev
        return tmp.value

    def insert(self, value, index):
        if index is 0 and self.first is not None:
            node = self.Node(value)
            tmp = self.first
            tmp.prev = node
            node.next = tmp
            self.first = node
        else:
            i = 0
            node = self.Node(value)
            tmp = self.first
            while i < index:
                tmp = tmp.next
                i += 1
            tmp.prev.next = node
            node.prev = tmp.prev
            tmp.prev = node
            node.next = tmp

    def contains(self, value):
        tmp = self.first
        while tmp.next is not None:
            if tmp.value is value:
                return True
            tmp = tmp.next
        return False

    def size(self):
        tmp = self.first
        i = 0
        while tmp.next is not None:
            i += 1
            tmp = tmp.next
        return i + 1

    def clear(self):
        self.first = None

    def __str__(self):
        tmp = self.first
        output = "["
        while tmp is not None:
            output += str(tmp.value) + ", "
            tmp = tmp.next
        return output[:-2] + "]"


if __name__ == "__main__":
    ll = LinkedList()
    ll.add(2)
    ll.add(3)
    ll.add(5)
    ll.add(10)
    ll.add('test')
    ll.add('hej')
    print(ll)
    print(ll.get(2))
    print(ll.get(1))
    try:
        print(ll.get(10))
    except IndexError as e:
        print(e.args)
    ll.remove('test')
    print(ll)
    ll.remove_at(2)
    print(ll)
    ll.insert(8, 2)
    print(ll)
    print(ll.contains(3))
    print(ll.contains(95))
    print(ll.size())

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
                return None
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
        tmp = tmp.next
        return None

    def remove_at(self, index):
        if self.first is None:
            return None
        tmp = self.first
        i = 0
        while i < index:
            tmp = tmp.next
            i += 1
            if tmp.next is not None:
                next = tmp.next
                prev = tmp.prev
                next.prev = prev
                prev.next = next
        return tmp.value

    def insert(self, value, index):
        if self.first is None:
            return None
        tmp = self.first
        i = 0
        while i < index:
            pass

    def contains(self, value):
        # TODO: implement this method
        pass

    def size(self):
        # TODO: implement this method
        pass

    def clear(self):
        # TODO: implement this method
        pass

    def __str__(self):
        return

if __name__ == "__main__":
    ll = LinkedList()
    ll.add(2)

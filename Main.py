#!/bin/python

class LinkedList(object):
    # Inner class
    class Node(object):
        prev = None
        next = None

        def __init__(self, value):
            self.value = value

    # LinkedList fields
    first = None

    # LinkedList methods
    def add(self, value):
        if self.first is None:
            node = self.Node(value)
            self.first = node
        else:
            tmp = self.first
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = self.node
        pass

    def get(self, index):

        pass

    def remove(self, value):

        pass

    def remove_at(self, index):
        # TODO: implement this method
        pass

    def insert(self, value, index):
        # TODO: implement this method
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
        pass


if __name__ == "__main__":
    ll = LinkedList()
    print(ll)
    # TODO: write "tests" as you implement different methods in your data structure
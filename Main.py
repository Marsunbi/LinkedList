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
                raise IndexError('Index out of bound. Index [{}]'.format(index))
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
            return node.value
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
            return node.value

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
    ll.add(5)
    ll.add(1)
    ll.add(10)
    ll.add(3)
    ll.add(5)
    ll.add(11)
    print("This is the linked list: {}".format(ll))
    print("")
    try:
        print("Here I get the number on index 4: \t\t\t [{}]".format(ll.get(4)))
        print("and on index 5: \t\t\t\t\t\t\t [{}]".format(ll.get(5)))
        ll.get(15)
    except IndexError as e:
        print(e.args)
    print("")
    print("This is the current linked list: \t\t\t {}".format(ll))
    print("The first node with value 5 is removed: \t {}".format(ll.remove(5)))
    print("The list after the node has been deleted: \t {}".format(ll))
    print("")
    print("The node at index 3 is deleted: \t\t\t {}".format((ll.remove_at(3))))
    print("The list after the node has been deleted: \t {} ".format(ll))
    print("")
    print("Node with value 8 inserted at index 2: \t\t {}".format(ll.insert(8, 2)))
    print("The lidt after the node has been added: \t {}".format(ll))
    print("")
    print("Check if the list contains value 5: \t\t {}".format(ll.contains(5)))
    print("Check if the list contains value 15: \t\t {}".format(ll.contains(15)))
    print("")
    print("The size of the linked list: \t\t\t\t {}".format(ll.size()))

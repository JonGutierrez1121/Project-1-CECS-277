from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i : int) -> Node:
        if i < 0 or i > self.n:
            return None
        if i < self.n/2:
            p = self.dummy.next
            for i in range(i):
                p = p.next
        else:
            p = self.dummy
            for i in range(self.n, i, -1):
                p = p.prev
        return p
        
    def get(self, i) -> np.object:
        if i < 0 or i >= self.n:
            raise IndexError()
        return self.get_node(i).x

    def set(self, i : int, x : np.object) -> np.object:
        if i < 0 or i >= self.n: raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = self.x
        return y

    def add_before(self, w : Node, x : np.object) -> Node:
        if w is None:
            raise IndexError()
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u
            
    def add(self, i: int, x : np.object):
        if i < 0 or i > self.n:
            raise IndexError()
        self.add_before(self.get_node(i), x)

    def remove(self, i: Node):
        w = self.get_node(i)
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1



    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)

    def isPalindrome(self) -> bool :
        # todo
        pass 


    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x

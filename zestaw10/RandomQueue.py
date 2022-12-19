import random

class Node:

    def __init__(self, data=None, next=None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

class RandomQueue:
    def __init__(self):
        self.guard = Node()   
        self.guard.next = self.guard
        self.guard.prev = self.guard
        self.random_node = self.guard

    def __str__(self):
        c = self.guard.prev
        queue_as_string = "["
        while c!= self.guard:
            queue_as_string += str(c)+" "
            c= c.prev
        queue_as_string += "]"
        return queue_as_string
        
    def randomize(self):
        if self.is_empty():
            raise IndexError("Cannot randomize empty queue!")
        possible_nodes = []
        if self.random_node.next != self.guard:
            possible_nodes.append(self.random_node.next)
        if self.random_node.prev != self.guard:
            possible_nodes.append(self.random_node.prev)
        if len(possible_nodes) != 0:
            self.random_node = random.choice(possible_nodes)

    def insert(self, item):    # wstawia element w czasie O(1)
        node = Node(item)
        node.next = self.guard.next
        node.prev = self.guard
        self.guard.next.prev = node
        self.guard.next = node
        self.randomize()

    def remove(self):# zwraca losowy element w czasie O(1)
        node = self.random_node
        self.randomize()
        self.randomize()
        self.randomize()
        data = self.remove_internal(node)
        return data

    def remove_internal(self,node):  
        if self.is_empty():
            raise IndexError("Cannot remove from empty queue!")
        data = node.data
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None  
        return data
        

    def is_empty(self):
        return self.guard.next == self.guard
    def is_full(self): 
        return False

    def toSet(self):
        wynik = set()
        c = self.guard.next
        while c!= self.guard:
            wynik.add(c.data)
            c= c.next
        return wynik
    def clear(self):
        self.guard = Node()
        self.guard.next = self.guard
        self.guard.prev = self.guard
        self.random_node = self.guard

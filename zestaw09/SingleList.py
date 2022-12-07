class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __eq__(self,other):
        if not isinstance(other,Node):
            return False
        return self.data == other.data

    def __ne__(self, other) -> bool:
        return not self == other

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head :Node = None
        self.tail :Node = None
    
    def __repr__(self):
        if self.head == None:
            return "None"
        return f"{self.head.data}...{self.length}...{self.tail} "

    def __eq__(self,other): #Funkcja pozwala na wykonanie testow
        if self.length != other.length:
            return False
        n = self.head
        k = other.head
        while(n!= None):
            if(n!=k):
                return False
            n = n.next
            k = k.next
        return True
    
    def __ne__(self,other):
        return not self == other

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):   # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node
    
    def remove_tail(self):   # klasy O(n)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.tail
        prev = self.head
        self.length -= 1
        if node == prev:
            self.head = None
        else:
            while(prev.next != node):
                prev = prev.next
        prev.next = None
        self.tail = prev
        return node
        
    def join(self, other : "SingleList"):   # klasy O(1)
        if other.head == None:
            return
        else:
            self.insert_tail(other.remove_head())
            self.join(other)


    def clear(self):   # czyszczenie listy
        while self.head != None:
            self.length -= 1
            t = self.head
            self.head = self.head.next
            del t
        self.tail = None
    
    def search(self, data):  # klasy O(n)
        cur = self.head
        while cur != None and cur.data != data:
            cur = cur.next
        return cur
    def find_min(self):   # klasy O(n)
        cur = self.head
        min = cur
        while cur != None:
            if min.data > cur.data:
                min = cur
            cur = cur.next
        return min
    
    def find_max(self):  # klasy O(n)
        cur = self.head
        max = cur
        while cur != None:
            if max.data < cur.data:
                max = cur
            cur = cur.next
        return max

    
    def reverse(self):   # klasy O(n)
        new_list = SingleList()
        while self.head != None:
            new_list.insert_head(self.remove_head())
        self = new_list
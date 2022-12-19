from RandomQueue import RandomQueue, Node
import pytest

class TestrandomQueue:

    def test_queue_push(self):
        queue = RandomQueue()
        queue.insert(1)
        queue.insert(2)
        queue.insert(3)
        queue.insert(4)
        queue.insert(5)
        queue.insert(6)
        queue.insert(7)
        queue.insert(8)
        queue.insert(9)
        queue.insert(10)
        assert str(queue) == "[1 2 3 4 5 6 7 8 9 10 ]"

    @pytest.fixture
    def qA(self):
        queue = RandomQueue()
        queue.insert(1)
        queue.insert(2)
        queue.insert(3)
        queue.insert(4)
        queue.insert(5)
        queue.insert(6)
        queue.insert(7)
        queue.insert(8)
        queue.insert(9)
        queue.insert(10)
        return queue

    #Usuwam elementy i dodaje je do jednego zbioru
    # Nastepnie sprawdzam czy elementy w zbiorze zgadzaja
    # sie z elementami w kolejce
    def test_pop(self,qA):
        setA = qA.toSet()
        usuniete_elementy = set()
        i =0
        while not qA.is_empty():
            val = qA.remove()
            usuniete_elementy.add(val)
            i+=1
        assert setA == usuniete_elementy            


    if __name__ == "__main__":
        pytest.main()

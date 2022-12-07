from SingleList import SingleList, Node
import pytest

class TestSingleList:
    @pytest.fixture
    def A(self):
        lista = SingleList()
        lista.insert_tail(Node(1))
        lista.insert_tail(Node(2))
        lista.insert_tail(Node(3))
        lista.insert_tail(Node(4))
        return lista
    @pytest.fixture
    def RA(self):
        lista = SingleList()
        lista.insert_head(Node(1))
        lista.insert_head(Node(2))
        lista.insert_head(Node(3))
        lista.insert_head(Node(4))
        return lista

    @pytest.fixture
    def B(self):
        lista = SingleList()
        lista.insert_tail(Node(1))
        lista.insert_tail(Node(2))
        return lista
    @pytest.fixture
    def C(self):
        lista = SingleList()
        lista.insert_tail(Node(1))
        lista.insert_tail(Node(2))
        lista.insert_tail(Node(3))
        return lista

    @pytest.fixture
    def D(self):
        lista = SingleList()
        lista.insert_tail(Node(1))
        lista.insert_tail(Node(2))
        lista.insert_tail(Node(3))
        lista.insert_tail(Node(4))
        lista.insert_tail(Node(1))
        lista.insert_tail(Node(2))
        lista.insert_tail(Node(1))
        lista.insert_tail(Node(2))
        lista.insert_tail(Node(3))
        lista.insert_tail(Node(1))
        return lista
        
    @pytest.fixture
    def R(self):
        lista = SingleList()
        lista.insert_tail(Node(7))
        lista.insert_tail(Node(9))
        lista.insert_tail(Node(5))
        lista.insert_tail(Node(4))
        lista.insert_tail(Node(2))
        lista.insert_tail(Node(3))
        lista.insert_tail(Node(4))
        lista.insert_tail(Node(11))
        lista.insert_tail(Node(7))
        lista.insert_tail(Node(5))
        return lista
    @pytest.fixture
    def RR(self):
        lista = SingleList()
        lista.insert_head(Node(7))
        lista.insert_head(Node(9))
        lista.insert_head(Node(5))
        lista.insert_head(Node(4))
        lista.insert_head(Node(2))
        lista.insert_head(Node(3))
        lista.insert_head(Node(4))
        lista.insert_head(Node(11))
        lista.insert_head(Node(7))
        lista.insert_head(Node(5))
        return lista

    @pytest.fixture
    def S(self):
        lista = SingleList()
        lista.insert_tail(Node(1))
        return lista

    @pytest.fixture
    def E(self):
        lista = SingleList()
        return lista

    def test_remove_tail(self,A,B,C,S,E):
        usuniete = A.remove_tail()
        assert usuniete.data == 4
        assert A == C
        #Sprawdzam na wypadek jakby porownanie list nie dzialalo prawidlowo
        assert not A == B 
        usuniete = B.remove_tail()
        assert usuniete.data == 2
        assert B.length == 1
        assert B.tail.data == 1
        assert B.head.data == 1
        assert B == S
        usuniete = S.remove_tail()
        assert S.length == 0
        assert S == E
        assert usuniete.data == 1
    
    def test_remove_empty(self,E):
        with pytest.raises(ValueError):
            E.remove_tail()

    def test_join(self,A,B,C,D,E,S):
        len = A.count() + B.count() + C.count() + S.count()
        A.join(B)
        assert B == E
        assert A.count() == 6
        A.join(C)
        A.join(S)
        A.join(E)
        assert A == D
        assert A.count() == len
        assert A.tail.data == 1 and A.head.data  == 1
        assert C.count() == 0
    def test_clear(self,S,E,D):
        D.clear()
        S.clear()
        E.clear()
        assert D.tail == None
        assert D.head == None
        assert D.count() == 0
        assert S.count() == 0
        assert E.count() == 0        
        assert S.head == None
        assert S.tail == None

    def test_search(self,D):
        assert D.search(2) == Node(2)
        assert D.search(22) == None
        assert D.search(1).next == Node(2)

    def test_find_min(self,R,A,S,E):
        assert R.find_min() == Node(2)
        assert A.find_min() == Node(1)
        assert S.find_min() == Node(1)
        assert E.find_min() == None
 
    def test_find_max(self,R,A,S,E):
        assert R.find_max() == Node(11)
        assert A.find_max() == Node(4)
        assert S.find_max() == Node(1)
        assert E.find_max() == None

    def reverse(self,A,R,RA,RR):
        A.reverse()
        R.reverse()
        assert A == RA
        assert R == RR

    if __name__ == "__main__":
        pytest.main()
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

    if __name__ == "__main__":
        pytest.main()
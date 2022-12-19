from Stack import Stack
import pytest

class TestStack:
    @pytest.fixture
    def A(self):
        stos = Stack(5)
        stos.push(1)
        stos.push(2)
        stos.push(3)
        stos.push(4)
        return stos


    @pytest.fixture
    def E(self):
        return Stack(2)

    def test_pop(self,A,E):
        assert A.pop() == 4
        assert A.pop() == 3
        assert A.pop() == 2
        assert A.pop() == 1
        with pytest.raises(IndexError):
            A.pop()
            E.pop()
        
    
    def test__push(self,E):
        E.push(1)
        E.push(2)
        with pytest.raises(IndexError):
            E.push(3)

    if __name__ == "__main__":
        pytest.main()
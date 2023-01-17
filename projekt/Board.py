
class Board:
    def __init__(self,x,y) -> None:
        self.rows = x
        self.colls = y
        self.cells = [[0 for _  in range(y)]for _ in range(x)]
        self.toUpsize = [0,0,0,0]
    def shift_right(self):
        for i in range(self.rows):
            self.cells[i].insert(0,0)
        self.colls += 1
    def shift_down(self):
        self.cells.insert(0,[0 for _ in range(self.colls)])
        self.rows += 1
    def shift_up(self):
        self.cells.append([0 for _ in range(self.colls)])
        self.rows += 1
    def shift_left(self):
        for i in range(self.rows):
            self.cells[i].append(0)
        self.colls += 1
    def set_cell(self,x,y):
        if(x<self.colls and y < self.rows):
            self.cells[x][y] = 1
        self.bound_check(x,y)
    def upScale(self):
        if self.toUpsize[0]>0:
            self.shift_right()
        if self.toUpsize[1]>0:
            self.shift_down()
        if self.toUpsize[2]>0:
            self.shift_left()
        if self.toUpsize[3]>0:
            self.shift_up()
        self.toUpsize = [0,0,0,0]
    def bound_check(self,y,x):
        if x < 2:
            self.toUpsize[0]+=1
        if y < 2:
            self.toUpsize[1]+=1
        if x >= self.colls-1:
            self.toUpsize[2]+=1
        if y >= self.rows-1:
            self.toUpsize[3]+=1

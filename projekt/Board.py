
class Board:
    def __init__(self,x,y) -> None:
        self.rows = x
        self.colls = y
        self.cells = [[0 for _  in range(y)]for _ in range(x)]
        self.toUpsize = [0,0,0,0]

    #Functions responsible for adding rows and collumns to already existing board
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
        if(x<self.rows and y < self.colls):
            self.cells[x][y] = 1
        self.bound_check(x,y)

    #Function that actually takes care of makeing board bigger
    # so cells dont go out of bounds
    def upScale(self):
        if self.toUpsize[0]>0:
            self.shift_right()
            self.shift_right()
        if self.toUpsize[1]>0:
            self.shift_down()
            self.shift_down()
        if self.toUpsize[2]>0:
            self.shift_left()
            self.shift_left()
        if self.toUpsize[3]>0:
            self.shift_up()
            self.shift_up()
        self.toUpsize = [0,0,0,0]

    #Sprawdza czy punkt jest blisko granic
    def bound_check(self,y,x):
        if x < 2:
            self.toUpsize[0]+=1
        if y < 2:
            self.toUpsize[1]+=1
        if x >= self.colls-1:
            self.toUpsize[2]+=1
        if y >= self.rows-1:
            self.toUpsize[3]+=1

    #Oblicza nastepna generacje
    def calculate_future(self):
        futurecells = Board(self.rows,self.colls)
        for i in range(self.rows):
            for j in range(self.colls):
                #Liczenie sadsiadow
                neighbours = 0
                for k in range(-1,2):
                    for h in range(-1,2):
                        if(i+k >= 0 and i+k<self.rows and j+h >=0 and j+h < self.colls ): 
                            if(  self.cells[i+k][j+h]==1 and not(h==0 and k==0)):
                                neighbours += 1
                if(self.cells[i][j]==1):
                    if neighbours == 3 or neighbours ==2:
                        futurecells.set_cell(i,j)
                else:
                    if neighbours == 3:
                        futurecells.set_cell(i,j)
        futurecells.upScale()
        return futurecells

    #Before starting first game iteration we check the borders 
    #   for any cell that could possibly go out of bounds in next generation
    def check_borders(self):
        for i in range(self.rows):
            for k in range(2):
                self.bound_check(k,i)
                self.bound_check(self.rows-1-k,i)
                self.bound_check(i,self.colls-1-k)
                self.bound_check(i,k)


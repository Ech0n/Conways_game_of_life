from Board import Board
import sys

class SaveLoadManager:
    def __init__(self):
        self.load_dir = None
        self.save_dir = None
        if(len(sys.argv)==2):
            self.load_dir = sys.argv[1]
        if(len(sys.argv)==3):
            self.load_dir = sys.argv[1]
            self.save_dir = sys.argv[2]
    def load_file(self):
        if(self.load_dir):
            x = 0
            y = 0
            with open(self.load_dir,"r") as file:
                x = int(file.readline())
                y = int(file.readline())
                plansza = Board(x,y)
                for line in file.readlines():
                    values = line.split()
                    plansza.cells[int(values[0])][int(values[1])] = 1
                return plansza
        return None

    def save(self,cells):
        if(self.save_dir ):
            with open(self.save_dir,"w+") as file:
                file.write(str(cells.colls)+"\n")
                file.write(str(cells.rows)+"\n")
                for i in range(cells.rows):
                    for j in range(cells.colls):
                        if(cells.cells[i][j]) == 1:
                            file.write(str(i)+" "+str(j)+"\n")
                file.close()    
        return None
        
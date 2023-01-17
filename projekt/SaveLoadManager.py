from tkinter import filedialog as fd
from Board import Board

class SaveLoadManager:
    def __init__(self):
        self.save_dir = "./saves"
    def load_file(self):
        filename = fd.askopenfilename(initialdir=self.save_dir)
        if(filename == ""):
            return None
        x = 0
        y = 0
        with open(filename,"r") as file:
            x = int(file.readline())
            y = int(file.readline())
            plansza = Board(x,y)
            for line in file.readlines():
                values = line.split()
                plansza.cells[int(values[0])][int(values[1])] = 1
            return plansza
    def save(self,cells):
        filename = fd.asksaveasfilename(initialdir=self.save_dir, initialfile="unnamed.save",defaultextension=".save")
        if(filename == ""):
            return
        with open(filename,"w+") as file:
            file.write(str(cells.colls)+"\n")
            file.write(str(cells.rows)+"\n")
            for i in range(cells.rows):
                for j in range(cells.colls):
                    if(cells.cells[i][j]) == 1:
                        file.write(str(i)+" "+str(j)+"\n")
            file.close()    
import pygame
import sys

class Board:
    def __init__(self,x,y) -> None:
        self.rows = x
        self.colls = y
        self.cells = [[0 for _  in range(y)]for _ in range(x)]
    def shift_right(self):
        for i in range(self.cells):
            self.cells[i].insert(0,0)
        self.colls += 1
    def shift_down(self):
        self.cells.insert(0,[0 for _ in range(len(self.cells[0]))])
        self.rows += 1
    def shift_up(self):
        self.cells.append([0 for _ in range(len(cells[0]))])
        self.rows += 1
    def shift_left(self):
        for i in range(self.cells):
            self.cells[i].append(0)
        self.colls += 1



bounds = [0,0,0,0]
def calculate_future(cells):
    futurecells = [[0 for _  in range(newcolls)]for _ in range(newrows)]
    for i in range(rows):
        for j in range(colls):
            #Liczenie sadsiadow
            neighbours = 0
            for k in range(-1,2):
                for h in range(-1,2):
                    if(i+k >= 0 and i+k<rows and j+h >=0 and j+h < colls ): 
                        if(  cells[i+k][j+h]==1 and not(h==0 and k==0)):
                            neighbours += 1
            if(cells[i][j]==1):
                if neighbours == 3 or neighbours ==2:
                    bound_check(i,j,futurecells)
                    futurecells[i][j] = 1

            else:
                if neighbours == 3:
                    bound_check(i,j,futurecells)
                    futurecells[i][j] = 1
    # print(futurecells)
    return futurecells
                


def bound_check(x,y,cells):
    if x < bounds[0]:
        shift_right(cells)
        bounds[0] = x
    if y < bounds[1]:
        shift_down(cells)
        bounds[1] = y
    if x > bounds[2]:
        shift_left(cells)
        bounds[2] = x
    if y > bounds[2]:
        shift_up(cells)
        bounds[2] = y

pygame.init()
size = (width,height) = (640,580)
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("Gra w Zycie")

board_margin = 7
border_width = 1

font = pygame.font.Font(None, 50)
start_text = "RUN"
button_col =  pygame.Color(0,255,255)
runnning = False
bounds = [-5,-5,5,5]

def next_generation(cells):
    pass
rows = abs(bounds[1]-bounds[3])
colls = abs(bounds[0]-bounds[2])
cells = [[0 for _  in range(colls)]for _ in range(rows)]
clock = pygame.time.Clock()

while True:
    screen.fill(pygame.Color("black"))
    size = (screen.get_width(),screen.get_height()-100)
    width, height = size
    #draw board
    board_size = min(size)

    edge = max(rows,colls)
    cell_size = int(board_size/edge)-border_width
    cell_with_border = cell_size + border_width

    screenrows = height//cell_with_border 
    screencolls = width//cell_with_border + 1

    for i in range(screenrows):
        for j in range(screencolls):
            r1 = pygame.Rect(cell_with_border*(j),cell_with_border*(i),cell_size,cell_size)
            col = pygame.Color(244,244,244)
            if(i< rows and j < colls):
                if cells[i][j] == 1:
                    col = pygame.Color(22,200,22)
            pygame.draw.rect(screen,col,r1)


    newrows = abs(bounds[1]-bounds[3])
    newcolls = abs(bounds[0]-bounds[2])

    text_surf = font.render(start_text, True,button_col)
    text_rect = text_surf.get_rect(center=(width // 2, 540))
    screen.blit(text_surf, text_rect)
    if runnning:
        cells = calculate_future(cells)
        clock.tick(2)
    rows = newrows
    colls = newcolls
    for event in pygame.event.get():   # pętla po liście zdarzeń (event list)
        if event.type == pygame.QUIT:   # QUIT Event
            pygame.quit()   # deaktywacja pygame
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[1]>480:
                runnning = True
                start_text = "RUNNING"
                button_col = pygame.Color(255,0,0)
            elif not runnning:
                x = (int)(pos[0]/cell_with_border)
                y = (int)(pos[1]/cell_with_border)
                if(x<colls and y < rows):
                    if(cells[y][x] == 1):
                        cells[y][x] = 0
                    else:
                        cells[y][x] = 1
                else:
                    pass
                        # bound_check(x,y)
    clock.tick(60)


    pygame.display.flip()
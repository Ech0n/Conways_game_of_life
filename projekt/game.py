import pygame
import sys
from Board import Board

bounds = [0,0,0,0]
def calculate_future(cells:Board):
    # futurecells = [[0 for _  in range(newcolls)]for _ in range(newrows)]
    futurecells = Board(cells.colls,cells.rows)
    for i in range(cells.rows):
        for j in range(cells.colls):
            #Liczenie sadsiadow
            neighbours = 0
            for k in range(-1,2):
                for h in range(-1,2):
                    if(i+k >= 0 and i+k<cells.rows and j+h >=0 and j+h < cells.colls ): 
                        if(  cells.cells[i+k][j+h]==1 and not(h==0 and k==0)):
                            neighbours += 1
            if(cells.cells[i][j]==1):
                if neighbours == 3 or neighbours ==2:
                    futurecells.set_cell(i,j)

            else:
                if neighbours == 3:
                    futurecells.set_cell(i,j)
    futurecells.upScale()
    # print(futurecells)
    return futurecells
                




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
# bounds = [-5,-5,5,5]

def next_generation(cells):
    pass
# rows = abs(bounds[1]-bounds[3])
# colls = abs(bounds[0]-bounds[2])
# cells = [[0 for _  in range(colls)]for _ in range(rows)]

cells = Board(10,10)

clock = pygame.time.Clock()

while True:
    screen.fill(pygame.Color("black"))
    size = (screen.get_width(),screen.get_height()-100)
    width, height = size
    #draw board
    board_size = min(size)

    edge = max(cells.rows,cells.colls)
    cell_size = int(board_size/edge)-border_width
    cell_with_border = cell_size + border_width

    screenrows = height//cell_with_border 
    screencolls = width//cell_with_border + 1

    for i in range(screenrows):
        for j in range(screencolls):
            r1 = pygame.Rect(cell_with_border*(j),cell_with_border*(i),cell_size,cell_size)
            col = pygame.Color(244,244,244)
            if(i< cells.rows and j < cells.colls and i >= 0 and j>= 0):
                # print(i,j, cells.rows,cells.colls,len(cells.cells),len(cells.cells[-1]))
                if cells.cells[i][j] == 1:
                    col = pygame.Color(22,200,22)
            pygame.draw.rect(screen,col,r1)


    text_surf = font.render(start_text, True,button_col)
    text_rect = text_surf.get_rect(center=(width // 2, 540))
    screen.blit(text_surf, text_rect)
    if runnning:
        cells = calculate_future(cells)
        clock.tick(2)


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
                if(x<cells.colls and y < cells.rows):
                    if(cells.cells[y][x] == 1):
                        cells.cells[y][x] = 0
                    else:
                        cells.set_cell(y,x)
                else:
                    pass
                        # bound_check(x,y)
    clock.tick(60)


    pygame.display.flip()
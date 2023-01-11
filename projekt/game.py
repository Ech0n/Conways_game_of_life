import pygame
import sys

bounds = [0,0,0,0]

def calculate_future(cells):
    futurecells = [[0 for _  in range(colls)]for _ in range(rows)]
    for i in range(cells):
        for j in range(cells):
            #Liczenie sadsiadow
                

def bound_check(x,y):
    if x < bounds[0]:
        bounds[0] = x
    if y < bounds[1]:
        bounds[1] = y
    if x > bounds[2]:
        bounds[2] = x
    if y > bounds[2]:
        bounds[2] = y

pygame.init()
size = (width,height) = (640,580)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Gra w Zycie")

board_margin = 7
border_width = 1

font = pygame.font.Font(None, 50)


runnning = False

def next_generation(cells):
    pass
rows = abs(bounds[1]-bounds[3])+(board_margin*2)
colls = abs(bounds[0]-bounds[2])+(board_margin*2)

cells = [[0 for _  in range(colls)]for _ in range(rows)]
clock = pygame.time.Clock()

while True:
    size = (screen.get_width(),screen.get_height()-100)

    #draw board
    board_size = min(size)
    rows = abs(bounds[1]-bounds[3])+(board_margin*2)
    colls = abs(bounds[0]-bounds[2])+(board_margin*2)


    edge = max(rows,colls)
    cell_size = int(board_size/edge)-border_width
    cell_with_border = cell_size + border_width
    for i in range(rows):
        for j in range(colls):
            r1 = pygame.Rect(cell_with_border*(j),cell_with_border*(i),cell_size,cell_size)
            col = pygame.Color(244,244,244)
            if cells[i][j] == 1:
                col = pygame.Color(22,200,22)
            pygame.draw.rect(screen,col,r1)
            #Calculate next turn behaviour
    text = "RUN"
    text_surf = font.render(text, True, pygame.Color(0,255,255))
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
            elif not runnning:
                x = (int)(pos[0]/cell_with_border)
                y = (int)(pos[1]/cell_with_border)
                if(x<colls and y < rows):
                    if(cells[y][x] == 1):
                        cells[y][x] = 0
                    else:
                        cells[y][x] = 1
                        # bound_check(x,y)
    clock.tick(60)



    pygame.display.flip()
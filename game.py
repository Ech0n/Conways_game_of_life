import pygame
import sys
from Board import Board
from SaveLoadManager import SaveLoadManager

###################
speedmodifier = 1.0 #standardowa predkosc gry
speedmodifierchange = 0.2 #tempo zmiany predkosci gry
default_border_width = 1 #Grubosc linii pomiedzy komorkanmi
border_zeroing_threshold = 65 #Moment zanikania granicy dla zwiekszenia czytelnosci
max_speed = 10
min_speed = 0.1
#########################

slmanager = SaveLoadManager()
pygame.init()

#Tworzenie okna gry
size = (width,height) = (640,580)
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("Gra w Zycie")

font = pygame.font.Font(None, 50)
start_text = "RUN"
button_col =  pygame.Color(255,255,255)
runnning = False

cells = Board(10,10)
clock = pygame.time.Clock()

while True:
    #Resetowanie ekranu
    screen.fill(pygame.Color("black"))

    size = (screen.get_width(),screen.get_height()-100)
    width, height = size
    board_size = min(size)
    if max( cells.rows , cells.colls) > border_zeroing_threshold:
        border_width = 0
    else:
        border_width = default_border_width

    edge = 0
    if(cells.colls/width > cells.rows/height):
        edge = cells.colls
    else:
        edge = cells.rows

    cell_size = int(board_size/edge)-border_width
    cell_with_border = cell_size + border_width

    screenrows = height//cell_with_border 
    screencolls = width//cell_with_border + 1
    left_padding = (screencolls - cells.colls)//2
    top_padding = (screenrows - cells.rows)//2
    for i in range(screenrows):
        for j in range(screencolls):
            r1 = pygame.Rect(cell_with_border*(j),cell_with_border*(i),cell_size,cell_size)
            col = pygame.Color(244,244,244)
            if(i-top_padding< cells.rows and j - left_padding< cells.colls and i >= top_padding and j>= left_padding):
                if cells.cells[i-top_padding][j-left_padding] == 1:
                    col = pygame.Color(22,200,22)


            pygame.draw.rect(screen,col,r1)

    #UI
    text_surf = font.render(start_text, True,button_col)
    text_rect = text_surf.get_rect(center=(width // 2, height+50))
    screen.blit(text_surf, text_rect)
    
    left_rect = text_surf.get_rect(center=(50, height+50))
    right_rect = text_surf.get_rect(center=(width - 80, height+50))
    left_button = font.render("      <<", True,button_col)
    right_button = font.render("          >>", True,button_col)
   

    if runnning:
        #Simulating next generation
        cells = cells.calculate_future()
        clock.tick(2*speedmodifier)

    else:
        left_button = font.render("LOAD", True,button_col)
        right_button = font.render("SAVE", True,button_col)

    screen.blit(left_button, left_rect)
    screen.blit(right_button, right_rect)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit() 
            sys.exit(0)
        elif event.type == pygame.VIDEORESIZE:
            nwidth, nheight = event.size
            if nwidth < 600:
                nwidth = 600
                screen = pygame.display.set_mode((nwidth,nheight), pygame.RESIZABLE)    
            if nheight < 400:
                nheight = 400
                screen = pygame.display.set_mode((nwidth,nheight), pygame.RESIZABLE)

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[1]>height :
                if pos[0] > 150 and pos[0]<width-150:
                    if not runnning:
                        runnning = True
                        cells.check_borders()
                        start_text = "RUNNING"
                        button_col = pygame.Color(255,0,0)

                elif pos[0]>width-150:
                    if runnning:
                        speedmodifier =min( 1.0+speedmodifierchange,max_speed)
                    else:
                        slmanager.save(cells)
                else:
                    if runnning:    
                        speedmodifier =max( speedmodifierchange,min_speed)
                    else:
                        loaded = slmanager.load_file()
                        if(loaded != None):
                            cells = loaded
            elif not runnning:
                x = (int)(pos[0]/cell_with_border)
                y = (int)(pos[1]/cell_with_border)
                
                while(x<left_padding):
                    cells.shift_right()
                    left_padding-=1
                while(y<top_padding):
                    cells.shift_down()
                    top_padding-=1
                while(x-left_padding>=cells.colls):
                    cells.shift_left()
                while(y-top_padding >= cells.rows):
                    cells.shift_up()

                if(cells.cells[y-top_padding][x-left_padding] == 1):
                    cells.cells[y-top_padding][x-left_padding] = 0
                else:
                    cells.set_cell(y-top_padding,x-left_padding)
                
                    
    clock.tick(60)


    pygame.display.flip()
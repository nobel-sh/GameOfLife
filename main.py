#-----------------------------------------------imports-------------------------------------------------
from random import random
from time import sleep
import pygame
import sys

#-------------------------------------COLORS-AND-DIMENSIONS---------------------------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


DIMENSION_OF_CELL = 15
MARGIN = 2
#-------------------------------------Arguments-Related-Stuff--------------------------------------------
def print_help():
    print("Usage: python3 main.py -h\n       python3 main.py -r [SIZE OF GRID]\n       python3 main.py -t [PATH TO TEXT FILE]\n")
    exit(-1)


#---------------------------------------Game-of-Life-Code-----------------------------------------------
def init_state(size):
    return [[0 for _ in range(size)]for _ in range(size)]

def random_state(state):
    for i in range(size):
        for j in range(size):
            state[i][j]=int(random()*10)%2
    return state

def no_of_neighbours(state,x,y):
    sum=0
    for i in range(-1,2):
        _x = x+i
        if _x<0 or _x>=size:
            continue
        for j in range(-1,2):
            _y = y+j
            if i==0 and j==0:
                continue
            if _y<0 or _y>=size:
                continue
            if state[_x][_y]:
                sum+=1
    return sum

def next_state(state):

    new_state = init_state(size)
    for i in range(size):
        for j in range(size):
            n = no_of_neighbours(state, i, j)
            if state[i][j]==1:
                if n>3 or n<2:
                    new_state[i][j]=0
                else:
                    new_state[i][j]=1
            else:
                if n==3:
                    new_state[i][j]=1

        
    return new_state


#--------------------------------------Start-Program---------------------------------------------------------
args = sys.argv[1:]

if '-h' in args:
    print_help()
    

if ('-r' in args and '-t' in args) or len(args)!=2:
    print("[*] Incorrect arguments provided")
    print("[*] Displaying the help message...")
    print_help()

size = 0

if '-r' in args:
    size = int(args[-1:][0])
    st = init_state(size)
    st = random_state(st)

if '-t' in args:
    name = args[-1:][0]
    print(name)
    with open(name,'r') as f:
        contents = f.readlines()
        l= len(contents)
        b = len(contents[0])-1
        size=max(l,b)
        st = init_state(size)
        for i in range(l):
            for j in range(b):
                st[i][j]=int(contents[i][j])




#Start Pygame
pygame.init()


WINDOW_SIZE = (size*(DIMENSION_OF_CELL+MARGIN)+MARGIN,size*(DIMENSION_OF_CELL+MARGIN)+MARGIN)
screen = pygame.display.set_mode(WINDOW_SIZE)


pygame.display.set_caption("Conway's Game Of Life")


clock = pygame.time.Clock()

done = False


while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            done = True
    
    #BACKGROUND COLOR
    screen.fill(BLACK)

    
    for row in range(size):
        for col in range(size):
            color = BLACK
            if st[row][col]==1:
                color=WHITE
            pygame.draw.rect(screen, color, [(MARGIN + DIMENSION_OF_CELL) * col + MARGIN,
                              (MARGIN + DIMENSION_OF_CELL) * row + MARGIN,
                              DIMENSION_OF_CELL,
                              DIMENSION_OF_CELL])
    #limiting fps
    clock.tick(60)

    #Update the screen
    pygame.display.flip()

    #get the new state
    st = next_state(st)
    #wait for t seconds
    sleep(0.1)

pygame.quit()

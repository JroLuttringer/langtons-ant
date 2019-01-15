import random
import os
import time

# Create a 2D Matrix (width * height)
width  = 75
height = 52
matrix = []
# case is either BLACK or WHITE
BLACK = "."
WHITE = "#"

#Init matrix value
matrix = [[BLACK] * width for _ in range(height)]
# ant position is random
ant_x = width//2#random.randint(0,width-1)
ant_y = height//2#random.randint(0,height-1)

# ant direction
RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
ant_direction = UP



# function draw
# draw the matrix
# print "#" if the case is black, "." otherwise
def draw():
    # clear screen
    os.system("clear")
    for i in range(0,height-1):
        for j in range(0,width-1):
            print(matrix[i][j], end="")
        print("\n", end = "")



# chg_ant_direction_right
# make the ant do a right turn
def chg_ant_direction_right():
    global ant_direction
    if ant_direction == UP:
        ant_direction = RIGHT
    elif ant_direction == RIGHT:
        ant_direction = DOWN
    elif ant_direction == DOWN:
        ant_direction = LEFT
    else:
        ant_direction = UP

#chg_ant_direction_left
#make the ant do a left turn
def chg_ant_direction_left():
    global ant_direction
    if ant_direction == UP:
        ant_direction = LEFT
    elif ant_direction == LEFT:
        ant_direction = DOWN
    elif ant_direction == DOWN:
        ant_direction = RIGHT
    else:
        ant_direction = UP

# switch_color
# switch the ant's current position color
def switch_color():
    global matrix
    if matrix[ant_y][ant_x] == WHITE:
        matrix[ant_y][ant_x] = BLACK
    else:
        matrix[ant_y][ant_x] = WHITE

#move
#makes the ant move one space
# space is cyclic, if the ant is of bound, it's teleported to the other side
def move():
    global ant_x, ant_y
    #print("Before {} {} {}".format(ant_x, ant_y, ant_direction))
    if ant_direction == UP:
        ant_y = (ant_y - 1) % height
        if ant_y < 0:
            ant_y = height -1
    elif ant_direction == DOWN:
        ant_y = (ant_y +1) % height
    elif ant_direction == RIGHT:
        ant_x = (ant_x+1) % width
    elif ant_direction == LEFT:
        ant_x = ant_x -1
        if ant_x < 0:
            ant_x = width - 1


nb_iteration = 12000
i = 0
infinite_loop = True

#infinite loop or iterations limited
while i < nb_iteration or infinite_loop:
    # if BLACK, 90°  left, switch color to white and move
    if matrix[ant_y][ant_x] == BLACK:
        chg_ant_direction_left()
    # if white, turn 90° right, swhitch to black and move
    else:
        chg_ant_direction_right()

    switch_color()
    move()
    i= i+1
    if infinite_loop:
        draw()
        time.sleep(0.01)

draw()

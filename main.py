import os
import time
maze =  [[1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,1,1],
        [1,0,1,0,0,0,0,0,0,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,1,0,1],
        [1,1,1,0,1,0,1,1,1,0,1],
        [1,0,0,0,1,0,1,0,0,0,0,4],
        [1,1,1,1,1,1,1,1,1,1,1]]

width = 11
height = 11

x = 1
y = 1
v = 0

def draw (maze):
    time.sleep(0.1)
    os.system('cls')
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i == y and j == x):
                print("oo", end="")
                continue
            if (maze[i][j] == 0):
                print ("  ", end="")
            elif (maze[i][j] == 1):
                print ("██", end="")
            elif (maze[i][j] == 4):
                print ("  ", end="")
            
        print()
step = 0        
while maze[y][x]!= 4:
    draw(maze)

    if (v == 0):
        if (maze[y][x+1] != 1):
            v = 3
        elif (maze[y-1][x] != 1):
            v = 0
        elif (maze[y][x - 1] != 1):
            v = 1
        else:
            v = 2

    elif (v == 1):
        if (maze[y-1][x] != 1):
             v = 0
        elif (maze[y][x-1] != 1):
            v = 1
        elif (maze[y + 1][x] != 1):
            v = 2
        else:
            v = 3

    elif (v == 2):
            if (maze[y][x - 1] != 1):
                v = 1
            elif (maze[y+1][x] != 1):
                v = 2
            elif (maze[y][x + 1] != 1):
                v = 3
            else:
                v = 0

    elif (v == 3):
            if (maze[y+1][x] != 1):
                v = 2
            elif (maze[y][x + 1] != 1):
                v = 3
            elif (maze[y-1][x] != 1):
                v = 0
            else:
                v = 1

    if (v == 0):
        y -= 1
        step +=1
    elif (v == 1):
        x -= 1
        step +=1
    elif (v == 2):
        y += 1
        step +=1
    else:
        x += 1
        step +=1

print (step)



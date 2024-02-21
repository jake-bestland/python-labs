# Challenge yourself and practice learning from outside resources
# by following this tutorial to build a maze generator:
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e
import random
import time
from colorama import init
from colorama import Fore, Back, Style

def printMaze(maze):
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				print(Fore.WHITE + str(maze[i][j]), end=" ")
			elif (maze[i][j] == 'c'):
				print(Fore.GREEN + str(maze[i][j]), end=" ")
			else:
				print(Fore.RED + str(maze[i][j]), end=" ")
			
		print('\n')

#find number of surrounding cells
def surroundingCells(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
        s_cells += 1

    return s_cells	

cell = 'c'
wall = 'w'
unvisited = 'u'
height = 11
width = 27
maze = []

#initialize colorama
init()

#denote all cells as unvisited
for i in range(0, height):
    line = []
    for j in range(0, width):
        line.append(unvisited)
    maze.append(line)

#random starting point and set to cell
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)

if starting_height == 0:
    starting_height += 1
if starting_height == height-1:
    starting_height -= 1

if starting_width == 0:
    starting_width += 1
if starting_width == width-1:
    starting_width -= 1
    
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height-1, starting_width])
walls.append([starting_height, starting_width-1])
walls.append([starting_height, starting_width+1])
walls.append([starting_height+1, starting_width])

maze[starting_height-1][starting_width] = 'w'
maze[starting_height][starting_width-1] = 'w'
maze[starting_height][starting_width+1] = 'w'
maze[starting_height+1][starting_width] = 'w'

while walls:
    rand_wall = walls[int(random.random()*len(walls))-1]
    
    #check if left wall
    if rand_wall[1] != 0:
        if maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c':
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:
                #denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'
                #mark new walls
                #upper cell
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])
                #bottom cell
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])
                #leftmost cell
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])
            #delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)
            continue
    #check if upper wall
    if rand_wall[0] != 0:
        if maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c':
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:
                #new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                #mark new walls
                #upper cell
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1], rand_wall[1] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])
                #leftmost cell
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])
                #rightmost cell
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])
            #delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)
            continue
    
    #check if bottom wall
    if rand_wall[0] != height-1:
        if maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c':
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:
                #new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                #mark new walls
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if (rand_wall[0]+1, rand_wall[1] not in walls):
                        walls.append([rand_wall[0]+1, rand_wall[1]])
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])
            #delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)   
            continue 
    #check if right wall
    if rand_wall[1] != width-1:      
        if maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c':
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:
                #new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'
                #new walls
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]+1, rand_wall[1]])
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])
            #delete wal
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)
            continue
    
    #delete the wall from list anyway
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)

#mark remaining unvisited cells as walls
for i in range(0, height):
    for j in range(0, width):
        if (maze[i][j] == 'u'):
            maze[i][j] = 'w'

#set entrance and exit
for i in range(0, width):
    if (maze[1][i] == 'c'):
        maze[0][i] = 'c'
        break

for i in range(width-1, 0, -1):
    if (maze[height-2][i] == 'c'):
        maze[height-1][i] = 'c'
        break

#print final maze
printMaze(maze)
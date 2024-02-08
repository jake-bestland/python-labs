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


cell = 'c'
wall = 'w'
unvisited = 'u'
height = 11
width = 27
maze = []

def init_maze(width, height):
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append('u')
        maze.append(line)

    return maze

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

maze[starting_height-1, starting_width] = wall
maze[starting_height, starting_width-1] = wall
maze[starting_height, starting_width+1] = wall
maze[starting_height+1, starting_width] = wall



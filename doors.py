# -*- coding: utf-8 -*-
"""
Created on Sat Jan 5 17:01:06 2019

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

Machine learning a doors maze with memory of past moves

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Doors Learning [Computer software]. Github repository <https://github.com/alanjpan/Doors-Learning>

Note this software's license is GNU GPLv3.
"""


import random

doors = [[0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
memory = []

choice = []
p = 0
def init():
    for i in doors:
        choice = []
        for j in i:
            p = random.randrange(0, 100, 1)
            choice.append(p)
        memory.append(choice)
    print(doors)
    print(memory)

init()

choose = 0
door = 0
level = 0
iterations = 0
while level != len(doors):
    choose = 0
    for i in range(len(memory[level])):
        if memory[level][i] > choose:
            choose = memory[level][i]
            door = i
    print('level: ' + str(level))
    print('door selected: ' + str(door))
    if doors[level][door] == 1:
        memory[level][door] += 10
        level += 1
    elif doors[level][door] == 0:
        memory[level][door] -= 10
        level = 0
    print(memory)
    iterations += 1
print('iterations taken: ' + str(iterations))

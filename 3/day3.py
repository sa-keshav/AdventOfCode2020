#!/usr/bin/env python3
import sys
from typing import List
sys.path.append("../")
import readFile

FILE = "input.txt"
#FILE = "test.txt"


def findTrees(right: int, down: int, input: List[str]):
    index = right
    ctr: int = 0
    for i in input[down::down]:
        position = index % len(i)
        s = i[position]
        if s == '#':
            ctr += 1
        index += right
    return ctr

input = readFile.readFile(FILE)
print("############## Day 2 ##############")
print()
print("Part1: ",findTrees(3,1, input))

output = findTrees(1,1,input) 
output *= findTrees(3,1,input) 
output *= findTrees(5,1,input)
output *= findTrees(7,1,input)
output *= findTrees(1,2,input)
print("Part2: ",output)
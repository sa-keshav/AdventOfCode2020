#!/usr/bin/env python3
import sys
sys.path.append("../")
import readFile
import copy

from typing import List, Tuple


FILE = "input.txt"
#FILE = "test.txt"


def countOccupiedSeats(elements: List[str]) -> int:
    ctr: int = 0
    for e in elements:
        if e == '#':
            ctr += 1
    return ctr


def findAdjacentIndices(i: int, j: int, m: int, n: int) -> List[Tuple[int, int]]:
    """
    find adjacent indices of an element with position (i, j) in a m * n matrix 
    """
    adjacent_indices = []

    if i > 0:
        adjacent_indices.append((i-1, j))        
    if i+1 < m:
        adjacent_indices.append((i+1, j))
    if j > 0:
        adjacent_indices.append((i, j-1))     
    if j+1 < n:
        adjacent_indices.append((i, j+1))
    if i >0 and j+1<n:
        adjacent_indices.append((i-1, j+1))
    if i+1 < m and j>0:
        adjacent_indices.append((i+1, j-1))
    if i > 0 and j > 0:
        adjacent_indices.append((i-1, j-1))
    if i+1 < m and j+1 < n:
        adjacent_indices.append((i+1, j+1))
    
    return adjacent_indices


def findAdjacentElements(neigbours: List[Tuple[int, int]], input:List[str]) -> List[str]:
    """ find adjacent elements of an element using the position of this elements
    """

    adjacent_elements = []

    for i, j in neigbours:
       adjacent_elements.append(input[i][j])

    return adjacent_elements


def process(input):
    copyOfInput = copy.deepcopy(input)
    m = len(input)
    n = len(input[0])

    changesCtr = 0
    for i in range(m):
        for j in range(n):
            e = input[i][j]
            indexOfNeighbours = findAdjacentIndices(i, j, m, n)
            neighbours = findAdjacentElements(indexOfNeighbours, input)
            if e == 'L' and countOccupiedSeats(neighbours) == 0 :
                copyOfInput[i][j] = '#'
                changesCtr +=1
            if e == '#' and countOccupiedSeats(neighbours) >= 4:
                copyOfInput[i][j] = 'L'
                changesCtr +=1
    return changesCtr, copyOfInput


input = readFile.readFile(FILE) # this function read the file as list of strings

for i in range(len(input)): # change the list of strings to the list of lists (two dimensional list)
  input[i] = list(input[i])



######part1############

changes, newInput = process(input)

while changes != 0:
    changes, newInput = process(newInput)

numberOfOccupiedSeats = 0

for i in newInput:
    numberOfOccupiedSeats += countOccupiedSeats(i)

print()
print("######## Day 8 #########")
print()
print("Part1: How many seats end up occupied? ", numberOfOccupiedSeats)
print()




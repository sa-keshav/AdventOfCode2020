#!/usr/bin/env python3
from typing import List, Tuple
import time
import copy
import sys
sys.path.append("../")
import readFile


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
    if i > 0 and j+1 < n:
        adjacent_indices.append((i-1, j+1))
    if i+1 < m and j > 0:
        adjacent_indices.append((i+1, j-1))
    if i > 0 and j > 0:
        adjacent_indices.append((i-1, j-1))
    if i+1 < m and j+1 < n:
        adjacent_indices.append((i+1, j+1))

    return adjacent_indices


def findAdjacentElements(neigbours: List[Tuple[int, int]], input: List[str]) -> List[str]:
    """ find adjacent elements of an element using the position of this elements
    """

    adjacent_elements = []

    for i, j in neigbours:
        adjacent_elements.append(input[i][j])

    return adjacent_elements


def processPart1(input):

    copyOfInput = copy.deepcopy(input)

    m = len(input)
    n = len(input[0])

    changesCtr = 0
    for i in range(m):
        for j in range(n):
            e = input[i][j]
            indexOfNeighbours = findAdjacentIndices(i, j, m, n)
            neighbours = findAdjacentElements(indexOfNeighbours, input)
            if e == 'L' and countOccupiedSeats(neighbours) == 0:
                copyOfInput[i][j] = '#'
                changesCtr += 1
            if e == '#' and countOccupiedSeats(neighbours) >= 4:
                copyOfInput[i][j] = 'L'
                changesCtr += 1
    return changesCtr, copyOfInput


def findFirstSeenSeats(x, y: int, input: List[str]) -> list[str]:

    # actual position (y,x)

    firstSeanSeats = []
    x_max = len(input[0])
    y_max = len(input)

    for i in range(x+1, x_max):  # x.......
        if input[y][i] != '.':
            firstSeanSeats.append(input[y][i])
            break
    for i in reversed(range(0, x)):  # .....x
        if input[y][i] != '.':
            firstSeanSeats.append(input[y][i])
            break
    for i in reversed(range(0, y)):  # .
        if input[i][x] != '.':       # x
            firstSeanSeats.append(input[i][x])
            break
    for i in range(y+1, y_max):                   # x
        if input[i][x] != '.':                  # .
            firstSeanSeats.append(input[i][x])
            break
    for i, j in zip(reversed(range(0, y)), reversed(range(0, x))):
        if input[i][j] != '.':
            firstSeanSeats.append(input[i][j])
            break
    for i, j in zip(range(y+1, y_max), range(x+1, x_max)):
        if input[i][j] != '.':
            firstSeanSeats.append(input[i][j])
            break
    for i, j in zip(reversed(range(0, y)), range(x+1, x_max)):
        if input[i][j] != '.':
            firstSeanSeats.append(input[i][j])
            break
    for i, j in zip(range(y+1, y_max), reversed(range(0, x))):
        if input[i][j] != '.':
            firstSeanSeats.append(input[i][j])
            break

    return firstSeanSeats

def processPart2(input: List[str]) -> Tuple[int, List[str]]:
    copyOfInput = copy.deepcopy(input)
    m = len(input)
    n = len(input[0])

    changesCtr : int = 0
    for i in range(m):
        for j in range(n):
            e = input[i][j]
            if e == '.':
                copyOfInput[i][j] = e
                continue
            neighbours = findFirstSeenSeats(j,i,input)
            if e == 'L' and countOccupiedSeats(neighbours) == 0:
                copyOfInput[i][j] = '#'
                changesCtr += 1
            elif e == '#' and countOccupiedSeats(neighbours) >= 5:
                copyOfInput[i][j] = 'L'
                changesCtr += 1
            else:
                copyOfInput[i][j] = e
    return changesCtr, copyOfInput

# this function read the file as list of strings
input = readFile.readFile(FILE)

# change the list of strings to the list of lists (two dimensional list)
for i in range(len(input)):
    input[i] = list(input[i])


######part1############
tic = time.perf_counter()

changes, newInput = processPart1(input)

while changes != 0:
    changes, newInput = processPart1(newInput)

numberOfOccupiedSeats = 0

for i in newInput:
    numberOfOccupiedSeats += countOccupiedSeats(i)

toc = time.perf_counter()

print()
print("######## Day 8 #########")
print()
print("Part1: How many seats end up occupied? ", numberOfOccupiedSeats)
print(f"This task took {toc - tic:0.4f} seconds")
print()

#################### part 2 #####################
tic = time.perf_counter()

numberOfChanges, newSeatLayout = processPart2(input)
while numberOfChanges != 0:
    numberOfChanges, newSeatLayout = processPart2(newSeatLayout)

numberOfOccupiedSeats = 0

for i in newSeatLayout:
    numberOfOccupiedSeats += countOccupiedSeats(i)

toc = time.perf_counter()

print()
print("######## Day 8 #########")
print()
print("Part2: How many seats end up occupied? ", numberOfOccupiedSeats)
print(f"This task took {toc - tic:0.4f} seconds")
print()

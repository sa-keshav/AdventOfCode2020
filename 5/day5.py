#!/usr/bin/env python3
import math
import sys
from typing import List
sys.path.append("../")
import readFile

FILE = "input.txt"
#FILE = "test.txt"

input = readFile.readFile(FILE)
seatIds : List[int] = []

for i in input:
    MIN_ROW = 0
    MAX_ROW = 127
    MIN_COLUMN = 0
    MAX_COLUMN = 7
    row = i[:6]
    for r in row:
        if r == 'F':
            MIN_ROW = MIN_ROW
            MAX_ROW = math.floor((MAX_ROW + MIN_ROW) / 2)
        if r == 'B':
            MIN_ROW = math.ceil((MAX_ROW + MIN_ROW) / 2)
            MAX_ROW = MAX_ROW
    if i[6] == 'F':
        row = MIN_ROW
    if i[6] == 'B':
        row = MAX_ROW
    column = i[7:]
    for c in column[:-1]:
        if c == 'L':
            MIN_COLUMN = MIN_COLUMN
            MAX_COLUMN = math.floor((MAX_COLUMN+MIN_COLUMN)/2)
        if c == 'R':
            MIN_COLUMN = math.ceil((MAX_COLUMN + MIN_COLUMN) /2)
            MAX_COLUMN = MAX_COLUMN
    if i[9] == 'L':
        column = MIN_COLUMN
    if i[9] == 'R':
        column = MAX_COLUMN
    seatId = (row * 8) + column
    seatIds.append(seatId)


maxSeatId = max(seatIds)
seatIds.sort()
mySeatId = sum(range(seatIds[0],seatIds[-1]+1)) - sum(seatIds)



print("############## Day 4 ##############")
print()
print("Part1: Max Seat ID: ", maxSeatId)
print()
print("Part2: My Seat ID: ", mySeatId)
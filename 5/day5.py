#!/usr/bin/env python3
import math
import sys
from typing import List
sys.path.append("../")
import readFile

FILE = "input.txt"
#FILE = "test.txt"
MIN_ROW = 0
MAX_ROW = 127
MIN_COLUMN = 0
MAX_COLUMN = 7

input = readFile.readFile(FILE)
seatIds : List[int] = []

def processStr(input: str, min: int, max: int, upper: str, lower: str) -> int:
    number : int = 0
    for r in input[:-1]:
        if r == lower:
            max = math.floor((max + min) / 2)
        if r == upper:
            min = math.ceil((max + min) / 2)
    if input[-1] == lower:
        number = min
    if input[-1] == upper:
        number = max
    return number


for i in input:
    row = i[:7]
    column = i[7:]

    row = processStr(row, MIN_ROW, MAX_ROW, upper = 'B', lower = 'F')
    column = processStr(column, MIN_COLUMN, MAX_COLUMN, upper = 'R', lower = 'L')

    seatId = (row * 8) + column
    seatIds.append(seatId)


maxSeatId = max(seatIds)
seatIds.sort()
mySeatId = sum(range(seatIds[0],seatIds[-1]+1)) - sum(seatIds)


print()
print("######## Day 4 #########")
print()
print("Part1: Max Seat ID: ", maxSeatId)
print()
print("Part2: My Seat ID: ", mySeatId)
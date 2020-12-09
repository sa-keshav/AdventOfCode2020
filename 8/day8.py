#!/usr/bin/env python3
import sys
from typing import List, Tuple
sys.path.append("../")
import readFile

FILE = "input.txt"
#FILE = "test.txt"


def process(input: List[str]) -> Tuple[int, bool]:
    acc: int = 0
    i = 0
    indexes = []
    while(i < len(input)):
        if i in indexes:
            return acc, False

        indexes.append(i)

        temp = input[i].split(" ")
        command = temp[0]
        argument = int(temp[1])

        if command == 'nop':
            i += 1
        if command == 'acc':
            i += 1
            acc += argument
        if command == 'jmp':
            i += argument

    return acc, True


input = readFile.readFile(FILE)
######part1############

acc, _ = process(input)

########part2##########

acc2: int = 0
for i in range(len(input)):

    temp = input[i].split(" ")
    command = temp[0]
    argument = temp[1]

    if command == 'acc':
        continue

    input_copy = input.copy()

    if command == 'nop':
        input_copy[i] = 'jmp '+argument

    if command == 'jmp':
        input_copy[i] = 'nop '+argument

    acc2, isLastAcc = process(input_copy)
    if isLastAcc:
        break


print()
print("######## Day 8 #########")
print()
print("Part1: Accumulator: ", acc)
print()
print("Part2: Accumulator: ", acc2)

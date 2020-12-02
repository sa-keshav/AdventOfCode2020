#!/usr/bin/env python3
import csv
from typing import List

FILE = "input.csv"
#FILE = "test.csv"

class Result:
    min: int
    max: int
    letter: str
    password: str


def readCSV(filename: str) -> List[Result]:
    result : List[Result]= []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            result.append(process(row[0]))

    return result

def process(input: str) -> Result:
    result = Result()

    temp = input.split("-", 1)
    result.min = int(temp[0])
    temp = temp[1].split(" ", 1)
    result.max = int(temp[0])
    temp = temp[1].split(":", 1)
    result.letter = temp[0]
    result.password = temp[1].replace(" ", "")

    return result
    
def part1(input: List[Result]) -> int:
    ctr: int = 0
    for i in input:
        count = i.password.count(i.letter)
        if count >= i.min and count <= i.max:
            ctr+=1
    return ctr

def part2(input:List[Result]) -> int:
    ctr: int = 0
    for i in input:
        position1 = i.min-1
        position2 = i.max-1
        found = [pos for pos, char in enumerate(i.password) if char == i.letter]
        if (position1 in found) ^ (position2 in found):
            ctr+=1
    return ctr

print("############## Day 2 ##############")
input = readCSV(FILE)
result1 = part1(input)
result2 = part2(input)
print()
print("Part1: ",result1)
print("Part2: ",result2)


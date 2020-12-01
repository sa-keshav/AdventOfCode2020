#!/usr/bin/env python3
import csv
from typing import List

RESULT : int = 2020
FILE = "input.csv"
#FILE = "test.csv"

def part1(input: List[int]) -> List[int]:
    output: List[int] = []

    for i in range(len(input)):
        a = input[i]
        for j in range(i+1, len(input)):
            b = input[j]
            if a + b == RESULT:
                output.append(a * b)
                print("a is: {}, b is: {}, a+b = {}".format(a, b, a+b))
    return output
    
def part2(input: List[int]) -> List[int]:
    output: List[int] = []

    for i in range(len(input)):
        a = input[i]
        for j in range(i+1, len(input)):
            b = input[j]
            for k in range(j+1, len(input)):
                c = input[k]
                if a + b + c == RESULT:
                    output.append(a * b * c)
                    print("a is: {}, b is: {}, c is: {}, a+b+c = {}".format(a, b, c, a+b+c))
    return output

def readCSV(filename: str) -> List[str]:
    result = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            result.append(int(row[0]))
    return result

################################# MAIN ###################################
input = readCSV(FILE)

result1 = part1(input)
print(result1)
result2 = part2(input)
print(result2)


    




  
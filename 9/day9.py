#!/usr/bin/env python3
import sys
from typing import List, Tuple
sys.path.append("../")
import readFile

FILE = "input.txt"
PREAMBLE_LENGTH: int = 25

#FILE = "test.txt"
#PREAMBLE_LENGTH: int = 5


def isIn(preamble: List[int], actual: int) -> bool:
    for j in range(len(preamble)):
        for element in range(j+1, len(preamble)):
            if actual == preamble[j] + preamble[element]:
                return True
    return False


def findFirstInvalidNumber(input: List[int]) -> int:
    for i in range(len(input[:-PREAMBLE_LENGTH])):
        preamble = input[i:i+PREAMBLE_LENGTH]
        actual = input[i+PREAMBLE_LENGTH]
        if not isIn(preamble=preamble, actual=actual):
            return actual


def findWeaknessList(input:List[int]) -> Tuple[bool, List[int]]:
    sum : int = 0
    for j in range(len(input)):
        sum += input[j] 
        if sum == firstInvalidNumber:
            return True, input[:j+1]
        if sum > firstInvalidNumber:
           return False, None 
    return False, None

input = readFile.readFile(FILE)
input = [int(i) for i in input] #convert list of str to int
firstInvalidNumber = findFirstInvalidNumber(input)

indexOfInvalidNumber = input.index(firstInvalidNumber)
newInput = input[:indexOfInvalidNumber]
weaknessList: List[int] = []

for i in range(len(newInput)):
    nextInput = newInput[i:]
    isWeaknessList, weaknessList = findWeaknessList(nextInput)
    if isWeaknessList:
        break

print(weaknessList)
result = max(weaknessList) + min(weaknessList)
print(result)
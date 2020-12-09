#!/usr/bin/env python3
import sys
from typing import List, Tuple
sys.path.append("../")
import readFile

FILE = "input.txt"
#FILE = "test.txt"
PREAMBLE_LENGTH: int = 25


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


input = readFile.readFile(FILE)
input = [int(i) for i in input]
print(findFirstInvalidNumber(input))

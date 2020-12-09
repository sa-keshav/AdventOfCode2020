#!/usr/bin/env python3
import sys
from typing import Dict, List
sys.path.append("../")
import readFile

FILE = "input.txt"
#FILE = "test.txt"

def split_list(input: List[str], delimiter: str) -> List[List[str]]:
    result: List[List[str]] = []
    while True:
        try:
            position = input.index(delimiter)
            result.append(input[:position])
            input = input[position+1:]
        except ValueError:
            break
    result.append(input)
    return result


input = readFile.readFile(FILE)
answers = split_list(input, "")
results: List[str] = []
sum1 : int = 0
sum2 = 0
for a in answers:
    temp = ''.join(a)
    temp = "".join(dict.fromkeys(temp))
    results.append(temp)
    sum1 += len(temp)


for group in answers:
    person_count = len(group)
    person = group[0]
    for question in person:
        ctr = 0
        for person_in in group[1:]:
            if question in person_in:
                ctr += 1
        if ctr == person_count-1:
            sum2 += 1 


print("SUM 1: ",sum1)
print("SUM 2:",sum2)
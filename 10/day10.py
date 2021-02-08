#!/usr/bin/env python3
import sys
from typing import List, Tuple
sys.path.append("../")
import readFile
from itertools import *

#FILE = "input.txt"
FILE = "test.txt"
#FILE = "test2.txt"

input = readFile.readFile(FILE)
input = [int(i) for i in input] #convert list of str to int
input.sort()
firstJoltage : int = 0
one_jolt_ctr: int = 0
three_jolt_ctr: int = 0

for i in input:
    #print(i)
    if i-firstJoltage == 1:
        one_jolt_ctr += 1
        firstJoltage += 1
    if i-firstJoltage == 3:
        three_jolt_ctr += 1
        firstJoltage += 3
three_jolt_ctr += 1
#print(one_jolt_ctr)
#print(three_jolt_ctr)
#print(one_jolt_ctr*three_jolt_ctr)
#print(input)

def isValidTuple(tuple: List) -> bool:
    for i in range(len(tuple)-1):
        if tuple[i+1] - tuple[i] > 3:
            return False
    return True

def removeInValidTuple(input: List[Tuple]) -> List[Tuple]:
    i = 0
    while i < len(input):
        if not isValidTuple(list(input[i])):
            del input[i]
        else:
            i +=1
    return input   
    

#result = permutations(input)
max_nr = max(input)
min_nr = min(input)
result = [seq for i in range(len(input), 0, -1) for seq in combinations(input, i) if sum(seq) > max_nr and seq[0] == min_nr and seq[-1] == max_nr ]
result.sort()


#print(len(result))

validTuple = removeInValidTuple(result)
#print(len(validTuple))

for r in validTuple:
   print("r is: ",r)

print(len(validTuple))
#print(result)


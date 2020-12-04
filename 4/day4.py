#!/usr/bin/env python3
import sys
from typing import Dict, List
sys.path.append("../")
import readFile
import string

FILE = "input.txt"
#FILE = "test.txt"

validKeys : List[str] = ['byr', 'iyr','eyr','hgt','hcl','ecl','pid'] 

def isValidDate(input: str, least: str, most: str) -> bool:
    return len(input) == 4 and input >= least and input <= most  

def isByr(input: str) -> bool:
    return isValidDate(input, '1920', '2002')

def isIyr(input: str) -> bool:
    return isValidDate(input, '2010', '2020')

def isEyr(input: str) -> bool:
    return isValidDate(input, '2020', '2030')

def isHgt(input: str) -> bool:
    nr: int = 0
    if 'cm' in input:
        nr = int(input[:input.find('cm')])
        return nr >= 150 and nr <= 193
    if 'in' in input:
        nr = int(input[:input.find('in')])
        return nr >= 59 and nr <= 76
    return False

def isHcl(input: str) -> bool:
    if len(input) ==7 and '#' in input:
        hairColor = input[1:]
        return all(c in string.hexdigits for c in hairColor)
    return False

def isEcl(input: str) -> bool:
    validColors :List[str] = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return input in validColors

def isPid(input: str) -> bool:
    return len(input) == 9 and input.isdigit()


valid : Dict[str, callable]= {
    'byr': isByr,
    'iyr': isIyr,
    'eyr': isEyr,
    'hgt': isHgt,
    'hcl': isHcl,
    'ecl': isEcl,
    'pid': isPid
}

def split_list(input: List[str], delimiter: str) -> List[List[str]]:
    result: List[List[str]] = []
    rounds = input.count(delimiter)
    for i in range(rounds):
        position = input.index(delimiter)
        element = input[:position]
        result.append(element)
        input = input[position+1:]      
    result.append(input) #take the last element too
    return result

def findElements(input: List[str]) -> List[List[str]]:
    return " ".join(input).split(" ")
    

def findValue(substr: str, input: List[str]) -> str:
    index = [i for i, elem in enumerate(input) if substr in elem]
    index = index[0]
    temp = input[index].split(":")
    return temp[1]

def makeMap(input: List[str]) -> dict[str, str]:
    map = {}
    for i in input:
        temp = i.split(":")
        map[temp[0]] = temp[1]
    return map

def isValidPart1(input: str) -> bool:
    input = findElements(input)
    map = makeMap(input)
    for k in valid.keys():
        if k not in map.keys():
            return False   
    return True

def isValidPart2(input: str) -> bool:
    input = findElements(input)
    map = makeMap(input)
    for k, v in valid.items():
        if k not in map.keys():
            return False

        if not v(map[k]):
            return False     
    return True



    
input = readFile.readFile(FILE)
elements = split_list(input, "")
ctr1 = ctr2 = 0
for e in elements:
    if isValidPart1(e):
        ctr1 += 1

for e in elements:
    if isValidPart2(e):
        ctr2 += 1

print("############## Day 4 ##############")
print()
print("Part1: ", ctr1)
print()
print("Part2: ", ctr2)
 


#!/usr/bin/env python3
import sys
from typing import Dict, List
sys.path.append("../")
import readFile
import string
from process import toMap

FILE = "input.txt"
#FILE = "test.txt"

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


def isValidPart1(passport: Dict[str, str]) -> bool:
    for k in valid.keys():
        if k not in passport.keys():
            return False   
    return True

def isValidPart2(passport: Dict[str, str]) -> bool:
    for k, v in valid.items():
        if k not in passport.keys():
            return False

        if not v(passport[k]):
            return False     
    return True



    
input = readFile.readFile(FILE)
passports = toMap(input)
ctr1 = ctr2 = 0
for p in passports:
    if isValidPart1(p):
        ctr1 += 1

for p in passports:
    if isValidPart2(p):
        ctr2 += 1

print("############## Day 4 ##############")
print()
print("Part1: ", ctr1)
print()
print("Part2: ", ctr2)
 


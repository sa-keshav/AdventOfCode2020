#!/usr/bin/env python3
import sys
from typing import List
sys.path.append("../")
import readFile

FILE = "input.txt"
#FILE = "test.txt"
BAG = "shiny gold"

input = readFile.readFile(FILE)


def findBag(input: List[str], color: str) -> List[str]:
    result = []
    for line in input:
        if color in line:
            index = line.find('contain')
            parent = line[:index-2]
            parent = parent.replace('bags', '').replace('bag', '').strip()
            if color not in parent:  # dont append parent itself
                result.append(parent)
                temp = findBag(input, parent)
                if len(temp) != 0:
                    result += temp

    result = list(set(result))  # remove duplicates
    return result


parents = findBag(input, BAG)
# print(len(parents))


def findBags(input: List[str], color: str) -> int:
    result = 0
    for line in input:
        line = line.split('contain')
        if color in line[0]:
            if 'no other bags' in line[1]:
                break
            childs = line[1].strip().replace('.', '').replace(
                'bags', '').replace('bag', '')
            childs = childs.split(', ')
            for c in childs:
                index = c.find(' ')
                number = int(c[:index])
                result += number + number*findBags(input, c[index+1:].strip())
            break
    return result


nr = findBags(input, BAG)
print(nr)

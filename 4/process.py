from typing import Dict, List


def toMap(input: List[str]) -> List[Dict]:
    results: List[Dict] = []
    elements = split_list(input, "")
    for e in elements:
        temp = " ".join(e).split(" ")
        results.append(makeMap(temp))

    return results


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


def makeMap(input: List[str]) -> dict[str, str]:
    map = {}
    for i in input:
        temp = i.split(":")
        map[temp[0]] = temp[1]
    return map

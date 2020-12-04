from typing import List

def readFile(file: str) -> List[str]:
    with open(file) as fp:
        lines = fp.read().splitlines()
    return lines
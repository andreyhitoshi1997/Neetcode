from typing import List
def contains_duplicate(self, nums:List[int]) -> bool:
    seen = {}

    for n in nums:
        if seen.get(n):
            return True
        seen[n] = 1
    return False    
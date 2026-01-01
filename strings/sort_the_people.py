# Problem: Sort the People
# LeetCode: https://leetcode.com/problems/sort-the-people/
# Approach: Pair heights with names and sort in descending order
# Time Complexity: O(n log n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(heights, names))
        people.sort(reverse=True)
        return [name for _, name in people]

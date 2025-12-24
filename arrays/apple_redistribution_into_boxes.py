from typing import List

# Problem: Apple Redistribution into Boxes
# LeetCode: https://leetcode.com/problems/apple-redistribution-into-boxes/
# Approach: Greedy (use boxes with largest capacity first)
# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        current_capacity = 0

        capacity.sort(reverse=True)

        for i, cap in enumerate(capacity):
            current_capacity += cap
            if current_capacity >= total_apples:
                return i + 1

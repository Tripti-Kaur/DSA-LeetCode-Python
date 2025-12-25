from typing import List

# Problem: Maximize Happiness of Selected Children
# LeetCode: https://leetcode.com/problems/maximize-happiness-of-selected-children/
# Approach: Greedy (pick highest happiness first with decreasing effect)
# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        total = 0
        decrement = 0

        for i in range(k):
            value = happiness[i] - decrement
            if value > 0:
                total += value
            decrement += 1

        return total

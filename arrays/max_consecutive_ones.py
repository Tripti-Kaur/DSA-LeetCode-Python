# Problem: Max Consecutive Ones
# LeetCode: https://leetcode.com/problems/max-consecutive-ones/
# Approach: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        max_ones = 0

        for i, val in enumerate(nums):
            if val == 0:
                max_ones = max(max_ones, i - left)
                left = i + 1

        return max(max_ones, len(nums) - left)

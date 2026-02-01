# Problem: Divide an Array Into Subarrays With Minimum Cost I
# LeetCode: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
# Approach: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)

        first = nums[0]
        remaining = nums[1:]

        second = min(remaining)
        remaining.remove(second)
        third = min(remaining)

        return first + second + third

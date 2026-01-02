# Problem: N-Repeated Element in Size 2N Array
# LeetCode: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# Approach: Use a set to detect the repeated element
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

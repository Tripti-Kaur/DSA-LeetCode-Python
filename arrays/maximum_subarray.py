from typing import List

# Problem: Maximum Subarray
# LeetCode: https://leetcode.com/problems/maximum-subarray/
# Approach: Kadane’s Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

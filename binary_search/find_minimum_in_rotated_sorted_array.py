from typing import List

# Problem: Find Minimum in Rotated Sorted Array
# LeetCode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Approach: Binary Search comparing mid with right
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

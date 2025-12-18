from typing import List

# Problem: Contains Duplicate
# LeetCode: https://leetcode.com/problems/contains-duplicate/
# Approach: Compare length of list with length of set
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

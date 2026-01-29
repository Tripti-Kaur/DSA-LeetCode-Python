# Problem: Remove Duplicates from Sorted Array
# LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0  # index of last unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1

# Problem: Remove Duplicates from Sorted Array II
# LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Approach: Two Pointers with Count Tracking
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0          # index of last valid element
        count = 1      # count of current element

        for i in range(1, len(nums)):
            if nums[i] == nums[j] and count < 2:
                j += 1
                nums[j] = nums[i]
                count += 1
            elif nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                count = 1

        return j + 1

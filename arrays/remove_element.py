# Problem: Remove Element
# LeetCode: https://leetcode.com/problems/remove-element/
# Approach: Two Pointers (Swap with End)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[j] == val:
                j -= 1
            elif nums[i] != val:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        return j + 1

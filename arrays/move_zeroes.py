from typing import List

# Problem: Move Zeroes
# LeetCode: https://leetcode.com/problems/move-zeroes/
# Approach: Two pointers – move non-zero elements forward
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1

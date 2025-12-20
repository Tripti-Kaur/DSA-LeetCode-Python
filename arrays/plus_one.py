from typing import List

# Problem: Plus One
# LeetCode: https://leetcode.com/problems/plus-one/
# Approach: Simulate carry from the end
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

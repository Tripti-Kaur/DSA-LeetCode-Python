from typing import List

# Problem: Count Negative Numbers in a Sorted Matrix
# LeetCode: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# LeetCode Daily Challenge
# Approach: Binary Search on each row
# Time Complexity: O(m log n)
# Space Complexity: O(1)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:
            left, right = 0, len(row) - 1

            # Find the first negative number in the row
            while left < right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid
                else:
                    left = mid + 1

            if row[left] < 0:
                count += len(row) - left

        return count

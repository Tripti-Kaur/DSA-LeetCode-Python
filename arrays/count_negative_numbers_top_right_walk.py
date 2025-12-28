from typing import List

# Problem: Count Negative Numbers in a Sorted Matrix
# LeetCode: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# LeetCode Daily Challenge
# Approach: Top-right walk (matrix traversal)
# Time Complexity: O(m + n)
# Space Complexity: O(1)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        r, c = 0, cols - 1
        count = 0

        while r < rows and c >= 0:
            if grid[r][c] < 0:
                # All elements below are also negative
                count += rows - r
                c -= 1
            else:
                r += 1

        return count

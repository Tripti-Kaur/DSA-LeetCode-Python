from typing import List

# Problem: Find a Peak Element II
# LeetCode: https://leetcode.com/problems/find-a-peak-element-ii/
# Approach: Binary search on columns + column maximum
# Time Complexity: O(n log m)
# Space Complexity: O(1)

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left, right = 0, len(mat[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            # Find row index of maximum element in mid column
            max_row = 0
            for r in range(len(mat)):
                if mat[r][mid] > mat[max_row][mid]:
                    max_row = r

            # Compare with right neighbor
            if mid + 1 < len(mat[0]) and mat[max_row][mid + 1] > mat[max_row][mid]:
                left = mid + 1
            # Compare with left neighbor
            elif mid > 0 and mat[max_row][mid - 1] > mat[max_row][mid]:
                right = mid - 1
            # Found peak
            else:
                return [max_row, mid]

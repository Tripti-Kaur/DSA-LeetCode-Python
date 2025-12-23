# Problem: First Bad Version
# LeetCode: https://leetcode.com/problems/first-bad-version/
# Approach: Binary search to find the first bad version
# Time Complexity: O(log n)
# Space Complexity: O(1)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

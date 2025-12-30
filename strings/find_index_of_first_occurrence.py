# Problem: Find the Index of the First Occurrence in a String
# LeetCode: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Time Complexity: O((n - m) * m)
# Space Complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1

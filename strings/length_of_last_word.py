from typing import List

# Problem: Length of Last Word
# LeetCode: https://leetcode.com/problems/length-of-last-word/
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

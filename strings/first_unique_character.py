# Problem: First Unique Character in a String
# LeetCode: https://leetcode.com/problems/first-unique-character-in-a-string/
# Approach: Frequency counting with two passes
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for index, ch in enumerate(s):
            if freq[ch] == 1:
                return index

        return -1

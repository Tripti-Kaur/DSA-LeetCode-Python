# Problem: Valid Anagram
# LeetCode: https://leetcode.com/problems/valid-anagram/
# Approach: Frequency counting using a dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Note:
# This solution supports Unicode characters since Python strings
# are Unicode by default and dictionaries can handle Unicode keys.
# Characters like 'é' and 'e' are treated as different characters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return False
            freq[ch] -= 1

        return True

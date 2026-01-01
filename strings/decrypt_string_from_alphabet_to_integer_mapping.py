# Problem: Decrypt String from Alphabet to Integer Mapping
# LeetCode: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
# Approach: Hash map + two-pointer parsing
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = {}

        for i in range(1, 27):
            if i <= 9:
                mapping[str(i)] = chr(96 + i)
            else:
                mapping[str(i) + "#"] = chr(96 + i)

        result = ""
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                result += mapping[s[i:i + 3]]
                i += 3
            else:
                result += mapping[s[i]]
                i += 1

        return result

from typing import List

# Problem: Longest Common Prefix
# LeetCode: https://leetcode.com/problems/longest-common-prefix/
# Approach: Shrinking prefix using startswith
# Time Complexity: O(n * m)
# Space Complexity: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

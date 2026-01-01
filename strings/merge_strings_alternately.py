# Problem: Merge Strings Alternately
# LeetCode: https://leetcode.com/problems/merge-strings-alternately/
# Approach: Two pointers, append characters alternately
# Time Complexity: O(n + m)
# Space Complexity: O(1) (excluding output)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        return result

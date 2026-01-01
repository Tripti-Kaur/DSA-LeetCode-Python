# Problem: Determine if String Halves Are Alike
# LeetCode: https://leetcode.com/problems/determine-if-string-halves-are-alike/
# Approach: Two pointers, count vowels in both halves
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = b = 0
        for i in range(len(s) // 2):
            if s[i] in "aeiouAEIOU":
                a += 1
            if s[-1 - i] in "aeiouAEIOU":
                b += 1
        return a == b

# Problem: Valid Palindrome II
# LeetCode: https://leetcode.com/problems/valid-palindrome-ii/
# Approach: Two Pointers with at most one deletion
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # Try skipping either left or right character
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            l += 1
            r -= 1

        return True

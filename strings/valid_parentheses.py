# Problem: Valid Parentheses
# LeetCode: https://leetcode.com/problems/valid-parentheses/
# Approach: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return not stack

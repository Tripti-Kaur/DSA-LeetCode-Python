# Problem: Count Asterisks
# LeetCode: https://leetcode.com/problems/count-asterisks/
# Approach: Toggle inclusion flag between pipe symbols
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def countAsterisks(self, s: str) -> int:
        include = True
        count = 0

        for ch in s:
            if ch == "|":
                include = not include
            elif ch == "*" and include:
                count += 1

        return count

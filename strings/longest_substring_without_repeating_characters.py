# Problem: Longest Substring Without Repeating Characters
# LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Approach: Sliding Window with Hash Map
# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))

from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: Dict[str, int] = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in last_seen:
                left = max(left, last_seen[char] + 1)

            last_seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length

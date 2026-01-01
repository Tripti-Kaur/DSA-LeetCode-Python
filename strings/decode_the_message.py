# Problem: Decode the Message
# LeetCode: https://leetcode.com/problems/decode-the-message/
# Approach: Build character substitution mapping from key
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        curr = ord('a')

        for ch in key:
            if ch != " " and ch not in mapping:
                mapping[ch] = chr(curr)
                curr += 1

        result = ""
        for ch in message:
            if ch == " ":
                result += " "
            else:
                result += mapping[ch]

        return result

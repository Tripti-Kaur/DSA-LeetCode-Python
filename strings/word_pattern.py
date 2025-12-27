# Problem: Word Pattern
# LeetCode: https://leetcode.com/problems/word-pattern/
# Approach: Bidirectional mapping
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        word_to_char = {}
        char_to_word = {}

        for i in range(len(words)):
            if words[i] in word_to_char:
                if word_to_char[words[i]] != pattern[i]:
                    return False
            else:
                word_to_char[words[i]] = pattern[i]

            if pattern[i] in char_to_word:
                if char_to_word[pattern[i]] != words[i]:
                    return False
            else:
                char_to_word[pattern[i]] = words[i]

        return True

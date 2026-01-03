# Problem: Sorting the Sentence
# LeetCode: https://leetcode.com/problems/sorting-the-sentence/
# Approach: Place words in correct index using the trailing digit
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        result = [""] * len(words)

        for word in words:
            idx = int(word[-1]) - 1
            result[idx] = word[:-1]

        return " ".join(result)

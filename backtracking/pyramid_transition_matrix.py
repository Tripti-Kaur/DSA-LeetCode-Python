import itertools
from typing import List

# Problem: Pyramid Transition Matrix
# LeetCode: https://leetcode.com/problems/pyramid-transition-matrix/
# LeetCode Daily Challenge
# Approach: Backtracking + recursion
# Time Complexity: Exponential (pruned by early stopping)
# Space Complexity: O(n) recursion depth

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Build transition map: pair -> list of possible top letters
        transitions = {}
        for rule in allowed:
            pair = rule[:2]
            top = rule[2]
            if pair not in transitions:
                transitions[pair] = []
            transitions[pair].append(top)

        def canBuild(row: str) -> bool:
            # Base case: reached the top
            if len(row) == 1:
                return True

            choices = []

            # Build choices for each adjacent pair
            for i in range(len(row) - 1):
                pair = row[i] + row[i + 1]
                if pair not in transitions:
                    return False
                choices.append(transitions[pair])

            # Try all possible next rows
            for next_row in map("".join, itertools.product(*choices)):
                if canBuild(next_row):
                    return True

            return False

        return canBuild(bottom)

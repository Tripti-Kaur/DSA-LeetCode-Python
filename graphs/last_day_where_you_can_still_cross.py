# Problem: Last Day Where You Can Still Cross
# LeetCode: https://leetcode.com/problems/last-day-where-you-can-still-cross/
# Approach: Binary Search on Days + BFS (Graph Traversal)
# Time Complexity: O((row * col) * log(row * col))
# Space Complexity: O(row * col)

from collections import deque
from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 0, len(cells)

        def canCross(blocked: set) -> bool:
            visited = set()
            queue = deque()

            # Start from all non-flooded cells in the top row
            for c in range(1, col + 1):
                if (1, c) not in blocked:
                    queue.append((1, c))
                    visited.add((1, c))

            # BFS traversal
            while queue:
                r, c = queue.popleft()

                # Reached bottom row
                if r == row:
                    return True

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        1 <= nr <= row and
                        1 <= nc <= col and
                        (nr, nc) not in blocked and
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return False

        # Binary search on the day
        while left <= right:
            mid = (left + right) // 2

            blocked = set()
            for r, c in cells[:mid]:
                blocked.add((r, c))

            if canCross(blocked):
                left = mid + 1
            else:
                right = mid - 1

        return right

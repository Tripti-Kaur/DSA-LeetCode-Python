from typing import List

# Problem: Magic Squares In Grid
# LeetCode: https://leetcode.com/problems/magic-squares-in-grid/
# Daily Challenge
# Time Complexity: O(m * n)
# Space Complexity: O(1)

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0

        def magicSquare(i: int, j: int) -> bool:
            seen = set()

            # Check range and uniqueness
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    v = grid[r][c]
                    if v < 1 or v > 9 or v in seen:
                        return False
                    seen.add(v)

            # Center must be 5
            if grid[i + 1][j + 1] != 5:
                return False

            # Check parity + sums
            if (
                grid[i][j] % 2 == 0 and
                grid[i][j + 2] % 2 == 0 and
                grid[i + 2][j] % 2 == 0 and
                grid[i + 2][j + 2] % 2 == 0 and

                grid[i][j + 1] % 2 != 0 and
                grid[i + 1][j] % 2 != 0 and
                grid[i + 1][j + 2] % 2 != 0 and
                grid[i + 2][j + 1] % 2 != 0 and

                sum(grid[i][j:j + 3]) == 15 and
                sum(grid[i + 1][j:j + 3]) == 15 and
                sum(grid[i + 2][j:j + 3]) == 15 and

                grid[i][j] + grid[i + 1][j] + grid[i + 2][j] == 15 and
                grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1] == 15 and
                grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2] == 15 and

                grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] == 15 and
                grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] == 15
            ):
                return True

            return False

        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if magicSquare(i, j):
                    count += 1

        return count

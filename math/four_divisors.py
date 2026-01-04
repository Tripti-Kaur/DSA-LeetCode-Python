# Problem: Four Divisors
# LeetCode: https://leetcode.com/problems/four-divisors/
# Approach: Count divisors using square root optimization
# Time Complexity: O(n * sqrt(m))
# Space Complexity: O(1)

from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            if num <= 2:
                continue

            divisors = {1, num}

            for d in range(2, int(num ** 0.5) + 1):
                if num % d == 0:
                    divisors.add(d)
                    divisors.add(num // d)

            if len(divisors) == 4:
                total += sum(divisors)

        return total

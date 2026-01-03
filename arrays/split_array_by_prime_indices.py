# Problem: Split Array by Prime Indices
# LeetCode: https://leetcode.com/problems/split-array-by-prime-indices/
# Approach: Use prime index check to split values into two groups
# Time Complexity: O(n * sqrt(n))
# Space Complexity: O(1)

from typing import List

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return abs(sum(nums))

        def isPrime(num: int) -> bool:
            if num < 2:
                return False
            if num == 2:
                return True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        A = 0
        B = nums[0] + nums[1]

        for i in range(2, len(nums)):
            if isPrime(i):
                A += nums[i]
            else:
                B += nums[i]

        return abs(A - B)

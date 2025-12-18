from typing import List

# Problem: Contains Duplicate II
# LeetCode: https://leetcode.com/problems/contains-duplicate-ii/
# Approach: Track last seen index using a hash map
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i

        return False

# Problem: Minimum Penalty for a Shop
# LeetCode: https://leetcode.com/problems/minimum-penalty-for-a-shop/
# LeetCode Daily Challenge
# Approach: Prefix + Suffix penalty calculation
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = []
        n_count = 0

        # Prefix penalty: count of 'N' before each hour
        for ch in customers:
            penalty.append(n_count)
            if ch == 'N':
                n_count += 1

        penalty.append(n_count)

        # Suffix penalty: count of 'Y' after each hour
        y_count = 0
        for i in range(len(customers) - 1, -1, -1):
            if customers[i] == 'Y':
                y_count += 1
            penalty[i] += y_count

        # Find earliest hour with minimum penalty
        best_hour = 0
        for i in range(len(penalty)):
            if penalty[i] < penalty[best_hour]:
                best_hour = i

        return best_hour

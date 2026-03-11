class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0

        for acc in accounts:
            s = sum(acc)

            if s > max:
                max = s

        return max
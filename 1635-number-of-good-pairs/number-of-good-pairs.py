from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)

        cnt = 0

        for c in counts:
            if counts[c] > 1:
                cnt += counts[c] * (counts[c] - 1) // 2

        return cnt


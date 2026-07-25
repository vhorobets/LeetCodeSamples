class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        
        cnt = 0
        for c in stones:
            if c in jewels_set:
                cnt += 1

        return cnt

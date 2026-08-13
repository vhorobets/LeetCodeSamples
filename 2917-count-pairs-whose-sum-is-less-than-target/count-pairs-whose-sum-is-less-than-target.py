class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        cnt = 0

        l = 0
        r = len(nums) - 1

        while l < r:
            while l < r and nums[l] + nums[r] >= target:
                r -= 1

            cnt += r - l
            l += 1
        
        return cnt


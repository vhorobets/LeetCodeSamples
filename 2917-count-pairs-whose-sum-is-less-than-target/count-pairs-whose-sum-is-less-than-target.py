class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        cnt = 0

        for l in range(len(nums)):
            r = len(nums) - 1

            while l < r and nums[l] + nums[r] >= target:
                r -= 1

            cnt += r - l
        
        return cnt


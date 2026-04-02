class Solution(object):
    def sortedSquares(self, nums):
        l = 0
        r = len(nums) - 1
        res = [0] * len(nums)
        idx = r

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[idx] = nums[l] ** 2
                l += 1
            else:
                res[idx] = nums[r] ** 2
                r -= 1

            idx -=1
        
        return res
        
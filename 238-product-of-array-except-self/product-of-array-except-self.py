class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [1] * n

        # calc direct, everything to the left of i
        current = 1
        for i in range(n):
            result[i] = current
            current *= nums[i]

        # calc back, everything to the right of i
        current = 1
        for i in range(n - 1, -1, -1):
            result[i] *= current
            current *= nums[i]

        return result
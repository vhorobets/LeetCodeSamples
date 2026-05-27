class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1] * n
        right = [1] * n

        current = 1
        for i in range(n):
            left[i] = current
            current *= nums[i]

        current = 1
        for i in range(n - 1, -1, -1):
            right[i] = current
            current *= nums[i]

        result = [1] * n
        for i in range(n):
            result[i] = left[i] * right[i]

        return result
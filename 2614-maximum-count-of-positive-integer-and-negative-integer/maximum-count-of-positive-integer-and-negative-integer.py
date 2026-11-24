class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] >= 0:
                r = mid - 1
            else:
                l = mid + 1
        
        num_negative = l

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid - 1

        num_positive = len(nums) - l

        return max(num_negative, num_positive)
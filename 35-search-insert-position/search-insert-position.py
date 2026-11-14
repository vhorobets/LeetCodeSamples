class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # [1,3,5,6]
        # l = 0 r = 3 -> 0 + (3 - 0) // 2 = 1 | item = 3
        # l = 2 r = 3 -> 2 + (3 - 2) // 2 = 1 | item = 3
        # l = 2
        #
        #
        #

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #     elif i == len(nums) - 1 and target > nums[i]:
        #         return len(nums)
        #     elif i == 0 and target < nums[i]:
        #         return 0
        #     elif nums[i] < target and target < nums[i + 1]:
        #         return i + 1

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l
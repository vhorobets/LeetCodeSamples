class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)

        if n == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1

        while i < n:
            correct_index = nums[i] - 1

            if 1 <= nums[i] <= n and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        m = max(nums)

        return n + 1 if n == m else n
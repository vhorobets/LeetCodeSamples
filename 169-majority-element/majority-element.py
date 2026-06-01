class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        target = len(nums) // 2

        for n in nums:
            dict[n] += 1
            if dict[n] > target:
                return n

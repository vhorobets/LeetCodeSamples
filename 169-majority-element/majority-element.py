class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = defaultdict(int)

        for n in nums:
            dict[n] += 1

        maxCount = 0
        maxKey = 0
        for key in dict.keys():
            if maxCount < dict[key]:
                maxCount = dict[key]
                maxKey = key

        return maxKey
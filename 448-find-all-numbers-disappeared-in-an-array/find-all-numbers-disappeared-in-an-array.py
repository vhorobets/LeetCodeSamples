class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n):
            index = abs(nums[i]) - 1
            nums[index] = -1 * abs(nums[index])

        #print(nums)

        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
 
        return res

                
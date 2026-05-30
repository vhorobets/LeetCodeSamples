class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, n = 0, len(nums)
        
        while i < n:
            if nums[i] == 0:
                curr_i = i
                j = i + 1
                while j < n:
                    nums[i], nums[j] = nums[j], nums[i]
                    j +=1
                    i +=1
                n -=1
                i = curr_i
            else:
                i += 1
        
        # 
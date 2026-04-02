class Solution(object):
    def removeElement(self, nums, val):
        l = 0
        r = len(nums) - 1

        while l <= r:
            if (nums[l] == val):
                while r > l and nums[r] == val:
                    r -= 1

                if (l < r):    
                    nums[l], nums[r] = (nums[r], nums[l])
                else:
                    break

            l += 1

        return l
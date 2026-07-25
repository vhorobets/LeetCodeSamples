class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # max_sum = 0

        # for i in range(k):
        #    max_sum += nums[i]

        # current_sum = max_sum
        # for i in range(k, len(nums)):
        #     current_sum -= nums[i - k]
        #     current_sum += nums[i]

        #     if current_sum > max_sum:
        #         max_sum = current_sum

        # return max_sum / k

        max_sum = current_sum = 0
        for i in range(len(nums)):
            if i < k:
                max_sum += nums[i]
                current_sum = max_sum
            else:
                current_sum -= nums[i - k]
                current_sum += nums[i]
                
                if current_sum > max_sum:
                    max_sum = current_sum

        return max_sum / k

    #O(n) - Time Complexity
    #O(1) - space complexity
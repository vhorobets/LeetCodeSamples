class Solution(object):
    def intersection(self, nums1, nums2):
        nums1_set = set(nums1)

        res = set()

        for n in nums2:
            if n in nums1_set:
                res.add(n)
        
        return list(res)

        
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = -1

        p1, p2 = 0, 0

        while p1 < len(nums1) and p2 < len(nums2):
            n1 = nums1[p1]
            n2 = nums2[p2]

            if n1 == n2:
                common = n1
                break
            elif n1 < n2:
                p1 += 1
            else:
                p2 += 1

        return common
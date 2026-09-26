class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashMap = {}
        stack = []

        for i in nums2:
            while stack and i > stack[-1]:
               hashMap[stack.pop()] = i  

            stack.append(i)
           
        for i in range(len(nums1)):
            nums1[i] = hashMap.get(nums1[i], -1)

        return nums1
        

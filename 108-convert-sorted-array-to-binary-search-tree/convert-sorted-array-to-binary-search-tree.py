# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.__buildNode(nums, 0, len(nums) - 1)

    def __buildNode(self, nums: List[int], leftIndex: int, rightIndex: int) -> Optional[TreeNode]:
        if leftIndex > rightIndex:
            return None

        middle = (leftIndex + rightIndex) // 2
        root = TreeNode(nums[middle])
        root.left = self.__buildNode(nums, leftIndex, middle - 1)
        root.right = self.__buildNode(nums, middle + 1, rightIndex)

        return root
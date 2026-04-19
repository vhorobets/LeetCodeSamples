# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.__sum_leaves_internal(root, True)
    
    def __sum_leaves_internal(self, root: Optional[TreeNode], isRight) -> int:
        if not root:
            return 0

        if not root.left and not root.right and not isRight:
            return root.val

        return self.__sum_leaves_internal(root.left, False) + self.__sum_leaves_internal(root.right, True)



        
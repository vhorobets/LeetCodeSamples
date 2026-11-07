# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.__minDepthInternal(root)
        
    def __minDepthInternal(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left:
            return 1 + self.__minDepthInternal(root.right)

        if not root.right:
            return 1 + self.__minDepthInternal(root.left)

        return 1 + min(self.__minDepthInternal(root.left), self.__minDepthInternal(root.right))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.__invert_internal(root)
        return root

    def __invert_internal(self, root: Optional[TreeNode]):
        if not root:
            return
        
        root.left, root.right = root.right, root.left

        self.__invert_internal(root.left)
        self.__invert_internal(root.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0

        def calcHeight(node):
            nonlocal max_length

            if not node:
                return 0

            left = calcHeight(node.left)
            right = calcHeight(node.right)

            max_length = max(max_length, left + right)

            return 1 + max(left, right)

        calcHeight(root)

        return max_length
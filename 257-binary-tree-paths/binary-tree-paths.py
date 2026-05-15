# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def appendPath(path, root: Optional[TreeNode]):
            if not root:
                return

            path = path + str(root.val)

            if not root.left and not root.right:
                res.append(path)
                return

            appendPath(path + "->", root.left)
            appendPath(path + "->", root.right)

        appendPath('', root)

        return res
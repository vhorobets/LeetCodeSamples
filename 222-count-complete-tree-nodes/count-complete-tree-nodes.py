# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        count = 0

        while queue:
            current = queue.popleft();
            count += 1

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return count
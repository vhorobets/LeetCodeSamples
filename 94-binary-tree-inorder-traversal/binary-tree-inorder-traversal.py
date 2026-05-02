# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def __add_node_value_internal_rec(root: Optional[TreeNode]):
            if not root:
                return

            __add_node_value_internal_rec(root.left)
            arr.append(root.val)
            __add_node_value_internal_rec(root.right)
        
        arr = []
        __add_node_value_internal_rec(root)
        return arr

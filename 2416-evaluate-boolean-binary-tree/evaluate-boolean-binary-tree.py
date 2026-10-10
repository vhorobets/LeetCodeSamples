# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:
        # def __evaluate(root: TreeNode | None) -> bool:
        #     if not root.left:
        #         return bool(root.val)

        #     operation = root.val
        #     if operation == 2:
        #         return __evaluate(root.left) or __evaluate(root.right)
        #     else:
        #         return __evaluate(root.left) and __evaluate(root.right)

        # return __evaluate(root)


        stack = [(root, False)]
        results = {}

        while stack:
            node, visited = stack.pop()

            if not node.left:
                results[node] = bool(node.val)
                continue

            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                left = results[node.left]
                right = results[node.right]

                if node.val == 2:
                    results[node] = left or right
                else:
                    results[node] = left and right

        return results[root]
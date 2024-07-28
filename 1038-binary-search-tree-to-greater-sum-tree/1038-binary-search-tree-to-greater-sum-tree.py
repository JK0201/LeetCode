# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dsf(root, total):
            if root == None:
                return total

            right = dsf(root.right, total)
            root.val += right
            left = dsf(root.left, root.val)

            return left

        dsf(root, 0)
        return root
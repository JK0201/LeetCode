class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        def dsf(root):
            nonlocal total

            if root == None:
                return

            dsf(root.right)
            total += root.val
            root.val = total
            dsf(root.left)

        dsf(root)
        return root
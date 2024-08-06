class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def postorder(cur_root):
            if cur_root == None:
                return 0

            left = postorder(cur_root.left)
            right = postorder(cur_root.right)

            return max(left, right) + 1

        return postorder(root)
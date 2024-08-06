class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        total = 0

        def preorder(cur_root, cur_depth):
            nonlocal max_depth, total

            if cur_root == None:
                return

            if cur_depth > max_depth:
                max_depth = cur_depth
                total = cur_root.val

            elif cur_depth == max_depth:
                total += cur_root.val

            preorder(cur_root.left, cur_depth + 1)
            preorder(cur_root.right, cur_depth + 1)

        preorder(root, 0)
        return total
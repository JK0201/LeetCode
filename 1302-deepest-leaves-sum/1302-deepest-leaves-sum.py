class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def postorder(cur_root):
            if cur_root == None:
                return (0, 0)

            left_val, left_depth = postorder(cur_root.left)
            right_val, right_depth = postorder(cur_root.right)

            if left_depth == 0 and right_depth == 0:
                return (cur_root.val, 1)

            elif left_depth > right_depth:
                return (left_val, left_depth + 1)

            elif left_depth < right_depth:
                return (right_val, right_depth + 1)

            return (left_val + right_val, left_depth + 1)

        return postorder(root)[0]
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        cnt = 0
        def postorder(cur_root):
            nonlocal cnt

            if cur_root == None:
                return (0, 0)

            left_val, left_total  = postorder(cur_root.left)
            right_val, right_total = postorder(cur_root.right)
            
            cur_val = left_val + right_val + cur_root.val
            cur_total = left_total + right_total + 1
            
            avg = int(cur_val / cur_total)
            if avg == cur_root.val:
                cnt += 1

            return (cur_val, cur_total)

        postorder(root)
        return cnt
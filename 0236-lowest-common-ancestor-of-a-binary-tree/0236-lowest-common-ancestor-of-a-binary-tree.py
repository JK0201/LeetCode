class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return

        left_node = self.lowestCommonAncestor(root.left, p, q)
        right_node = self.lowestCommonAncestor(root.right, p, q)

        if root == p or root == q:
            return root

        if left_node and right_node:
            return root

        elif left_node and not right_node:
            return left_node

        elif right_node and not left_node:
            return right_node
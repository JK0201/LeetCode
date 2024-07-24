# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, cur_node, p, q):
        if cur_node == None:
            return

        left_node = self.dfs(cur_node.left, p, q)
        right_node = self.dfs(cur_node.right, p, q)

        if cur_node.val == p.val or cur_node.val == q.val:
            return cur_node

        if left_node and right_node:
            return cur_node

        elif left_node and not right_node:
            return left_node

        elif right_node and not left_node:
            return right_node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
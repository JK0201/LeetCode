class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def postorder(cur_node):
            if cur_node == None:
                return

            left = postorder(cur_node.left)
            right = postorder(cur_node.right)

            if cur_node == p or cur_node == q:
                return cur_node

            elif left and right:
                return cur_node

            return left or right
        
        return postorder(root)
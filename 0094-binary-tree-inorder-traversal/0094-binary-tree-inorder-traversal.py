class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(cur_node):
            if cur_node == None:
                return

            inorder(cur_node.left)
            res.append(cur_node.val)
            inorder(cur_node.right)
        
        inorder(root)
        return res
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        
        def inorder(root):
            if root == None:
                return

            inorder(root.left)
            li.append(root.val)
            inorder(root.right)

        inorder(root)
        return li
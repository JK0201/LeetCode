class Solution:
    def inorder(self, root, li):
        if root == None:
            return
        
        self.inorder(root.left, li)
        li.append(root.val)
        self.inorder(root.right ,li)
        
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        self.inorder(root, li)

        return li
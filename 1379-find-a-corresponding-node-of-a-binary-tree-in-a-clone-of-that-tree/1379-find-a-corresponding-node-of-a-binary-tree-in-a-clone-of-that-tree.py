class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def postorder(cur_root):
            if cur_root == None:
                return

            left = postorder(cur_root.left)
            right = postorder(cur_root.right)

            if cur_root.val == target.val:
                return cur_root

            return left or right

        return postorder(cloned)
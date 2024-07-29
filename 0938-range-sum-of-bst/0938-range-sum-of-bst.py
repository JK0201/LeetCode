from collections import deque

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0

        if root == None:
            return

        q = deque([root])

        while q:
            cur_node = q.popleft()
            
            if cur_node.val >= low and cur_node.val <= high:
                total += cur_node.val

            if cur_node.left:
                q.append(cur_node.left)

            if cur_node.right:
                q.append(cur_node.right)

        return total
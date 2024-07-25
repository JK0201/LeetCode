from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = []

        if root == None:
            return 0

        q = deque()
        q.append((root, 1))

        while q:
            cur_node, cur_depth = q.popleft()
            depth.append(cur_depth)

            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))

            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))

        return max(depth)
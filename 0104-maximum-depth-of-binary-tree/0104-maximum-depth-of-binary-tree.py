from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = []

        if root == None:
            return 0

        q = deque()
        q.append((root, 1))

        while q:
            cur_node = q.popleft()
            depth.append(cur_node[1])

            if cur_node[0].left:
                q.append((cur_node[0].left, cur_node[1] + 1))

            if cur_node[0].right:
                q.append((cur_node[0].right, cur_node[1] + 1))

        return max(depth)
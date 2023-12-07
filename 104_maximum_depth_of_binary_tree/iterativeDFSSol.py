# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS Solution

        # If the root is null
        if not root:
          return 0

        # Initializing our stack and our result value
        stack = [[root, 1]]
        res = 1

        # We go through our entire stack
        while stack:
          # We pop the topmost value from our stack and get its node and depth
          node, depth = stack.pop()

          # Next we check if the node is null or not
          if node:
            # Get the maximum depth
            res = max(res, depth)
            # If not null, then get its children and add them to our stack. Update the depth as well
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

        return res


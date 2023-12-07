# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative BFS Solution

        # We check if our root is null
        if not root:
          return 0

        # Initialize our queue
        queue = deque([root])
        level = 0

        # while our queue is not empty
        while queue:
          # We go through each element in the queue
          for i in range(len(queue)):
            # We need to pop the leftmost element from the queue
            element = queue.popleft()
            # We then check if this element belongs to left or right children of root
            if element.left:
              queue.append(element.left)
            if element.right:
              queue.append(element.right)
          
          # We increment the level 
          level += 1
        return level


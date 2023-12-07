# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If our root is Null, then we have to return 0
        if not root:
            return 0

        # For any recurisve problem, we always consider the sub problem
        # thus, the 1 we have is for the root node, then we consider its children
        # and get the depth of each sub-tree by doing the following below
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Time Complexity: O(n) and Space Complexity: O(n)

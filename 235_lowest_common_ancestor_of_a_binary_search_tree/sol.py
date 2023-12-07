# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # We are going to use a pointer to find the LCA
        curr = root

        # Now we traverse the BST, we are assuming it never to be null
        while curr:
          # Now we check whether our curr is less than or greater than p and q in BST
          # If greater, then move left as we will find our LCA in the left subtree
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
          # If lesser, then move right
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
          # If the curr itself is p or q or if we find the parent of p and q then we return curr
            else:
                return curr


        

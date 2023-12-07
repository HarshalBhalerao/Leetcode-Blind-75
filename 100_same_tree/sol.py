# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Base case 1: If p and q are null, then return true as the tree is same
        if not p and not q:
            return True
        
        # Base case 2: If p is null or q is null, then return false as the trees are different
        # Base case 3: If either is not null, then we check for equal values. If p.val is not equal to q.val then we return false
        if not p or not q or p.val != q.val:
            return False

        # Call it recursively for left and right subtree
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
            
        

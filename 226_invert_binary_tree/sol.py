# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # If our root is null then we return null
        if not root:
            return None

        # We swap the positions of the childrens 
        temp = root.left
        root.left = root.right
        root.right = temp

        # As we are conducting DFS we then have to go down each of the respective sub-trees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



        

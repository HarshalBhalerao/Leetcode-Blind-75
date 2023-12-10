"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # This is our old to new hashmap, we are going to link the old hashmap to the newer hashmap.
        oldToNew = {}

        def dfs(node):
            # If the node already exists in oldToNew then made a clone of it. Thus, we just return the clone
            if node in oldToNew:
                return oldToNew[node]

            if node: 
                # We create a copy of the node
                cloneNode = Node(node.val)
                # Then map our cloneNode to the older node
                oldToNew[node] = cloneNode

                # Now we search for its neighbours and we add those to our cloneNode's neighbours
                for neighbourNode in node.neighbors:
                    cloneNode.neighbors.append(dfs(neighbourNode))

                return cloneNode
            else: 
                return None

        return dfs(node)

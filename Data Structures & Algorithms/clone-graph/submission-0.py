"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        myMap = {}
        return self.dfs(node, myMap)
    
    def dfs(self, node, myMap):
        if node in myMap:
            return myMap[node]
        myCopy = Node(node.val)
        myMap[node] = myCopy

        for neighbor in node.neighbors:
            myCopy.neighbors.append(self.dfs(neighbor, myMap))
        return myCopy
        

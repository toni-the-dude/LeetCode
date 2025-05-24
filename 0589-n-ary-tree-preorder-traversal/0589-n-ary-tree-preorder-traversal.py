"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def traverse(root):
            if not root: return []

            result = [root.val]

            for child in root.children:
                result += traverse(child)
                
            return result

        return traverse(root)
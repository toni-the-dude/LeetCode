# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(root):
            if not root: 
                return 0
            if root.val >= low and root.val <= high:
                return root.val + traverse(root.left) + traverse(root.right)
            return traverse(root.left) + traverse(root.right) 

        return traverse(root)
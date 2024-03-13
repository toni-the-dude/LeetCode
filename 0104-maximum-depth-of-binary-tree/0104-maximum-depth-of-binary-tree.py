# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):

        try:
            left_depth = 1 + self.maxDepth(root.left) * int(not root.left == None)
        except AttributeError:
            return 0

        try:
            right_depth = 1 + self.maxDepth(root.right) * int(not root.right == None)
        except AttributeError:
            return 0

        return max(left_depth, right_depth)


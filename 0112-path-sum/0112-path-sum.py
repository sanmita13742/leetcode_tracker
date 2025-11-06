# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        new_target = targetSum - root.val
        if new_target == 0 and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, new_target) or self.hasPathSum(root.right, new_target)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        if not root:
            return False
        if dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

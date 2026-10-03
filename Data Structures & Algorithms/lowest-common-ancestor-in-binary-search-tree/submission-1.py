# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root

        def findSplit(root):
            nonlocal res
            if not root:
                return

            if root.val>p.val and root.val>q.val:
                findSplit(root.left)
            elif root.val<p.val and root.val<q.val:
                findSplit(root.right)
            else:
                res = root
                
        findSplit(root)
        return res
        
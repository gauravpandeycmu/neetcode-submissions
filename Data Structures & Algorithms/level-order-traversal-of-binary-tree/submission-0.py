# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))

        height = height(root)
        ans = [[] for _ in range(height)]
        
        def helper(root, level):
            if root:
                ans[level].append(root.val)
                helper(root.left, level+1)
                helper(root.right, level+1)
        helper(root, 0)
        return ans

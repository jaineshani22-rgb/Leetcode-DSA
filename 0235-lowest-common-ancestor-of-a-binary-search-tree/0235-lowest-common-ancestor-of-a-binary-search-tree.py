# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # If both nodes are smaller, go left
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # If both nodes are larger, go right
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Otherwise, we found the split point (LCA)
            else:
                return curr
                
        return None
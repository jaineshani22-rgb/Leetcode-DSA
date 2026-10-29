# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        # Returns a tuple: (rob_current, skip_current)
        def dfs(node: Optional[TreeNode]) -> tuple:
            if not node:
                return (0, 0)
                
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            
            # If we rob this node, we must skip its children
            rob_current = node.val + left_skip + right_skip
            
            # If we skip this node, we take the max of robbing or skipping each child
            skip_current = max(left_rob, left_skip) + max(right_rob, right_skip)
            
            return (rob_current, skip_current)
            
        return max(dfs(root))
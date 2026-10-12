# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0
            
        # Helper to compute the height by going all the way left
        def get_left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
            
        left_height = get_left_height(root.left)
        right_height = get_left_height(root.right)
        
        # If left and right subtree left-heights are equal, the left subtree is a perfect binary tree
        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            return (1 << right_height) + self.countNodes(root.left)
       
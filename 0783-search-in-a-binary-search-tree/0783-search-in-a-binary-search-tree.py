# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        
        # Since it's a BST, if val is smaller, it must be in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If val is greater, it must be in the right subtree
        return self.searchBST(root.right, val)
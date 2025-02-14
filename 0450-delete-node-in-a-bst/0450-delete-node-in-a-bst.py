# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Recur down the tree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted is found
            
            # Case 1: Node has no child or only one child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 2: Node has two children
            # Find the inorder successor (smallest value in the right subtree)
            successor = self.findMin(root.right)
            
            # Copy the inorder successor's value to the current node
            root.val = successor.val
            
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, successor.val)
        
        return root
    
    def findMin(self, node: TreeNode) -> TreeNode:
        # The minimum value node is the leftmost leaf
        while node.left:
            node = node.left
        return node
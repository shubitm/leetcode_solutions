class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(root):
            leaves = []    
            def dfs(node):
                if node:
                    if not node.left and not node.right:
                        leaves.append(node.val)
                    dfs(node.left)
                    dfs(node.right)
            dfs(root)
            return leaves
        leaves1 = getLeaves(root1)
        leaves2 = getLeaves(root2)
        return leaves1 == leaves2
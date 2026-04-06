# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, res):
            if not node:
                return
            
            # Append current node value to the path
            path += str(node.val)
            
            # If it's a leaf node, add the completed path to our result list
            if not node.left and not node.right:
                res.append(path)
            else:
                # If not a leaf, continue DFS and add the arrow "->"
                dfs(node.left, path + "->", res)
                dfs(node.right, path + "->", res)
                
        result = []
        dfs(root, "", result)
        return result
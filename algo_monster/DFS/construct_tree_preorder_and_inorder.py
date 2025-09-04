"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
from aux import TreeNode

class Solution:
    def construct(self, preorder: list[int], inorder: list[int]) -> TreeNode:

        inorder_idx_map = {val:i for i, val in enumerate(inorder)}

        self.i = 0

        def dfs(start: int, end: int):

            if start > end:
                return None
            
            root_val = preorder[self.i]
            self.i += 1

            root = TreeNode(root_val)
            new_root = inorder_idx_map[root_val]
            root.left = dfs(start, new_root - 1)
            root.right = dfs(new_root + 1, end)

            return root

        return dfs(0, len(inorder) - 1)

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    tree = Solution().construct(preorder, inorder)
    print(tree.left.val)

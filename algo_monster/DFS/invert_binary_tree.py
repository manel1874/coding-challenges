"""Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

https://leetcode.com/problems/invert-binary-tree/description/
"""

from aux import TreeNode

class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            
            if node is None:
                return None

            new_node = TreeNode(node.val)
            new_node.left = dfs(node.right)
            new_node.right = dfs(node.left)

            return new_node

        return dfs(root)

if __name__ == "__main__":
    lor = [4,2,7,1,3,6,9]
    root = TreeNode.lor2tree(lor)
    inv_root = Solution().invert_tree(root)
    print(inv_root.right.val)
"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

from aux import TreeNode

class Solution:
    def max_depth(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode, level: int):
            if node is None:
                return level
            
            current_level = level + 1
            left_max_level = dfs(node.left, current_level)
            right_max_level = dfs(node.right, current_level)

            return max(left_max_level, right_max_level)

        initial_level = 0
        return dfs(root, initial_level)
    

if __name__ == "__main__":
    lor = [3,9,20,None,None,15,7]
    root = TreeNode.lor2tree(lor)
    depth = Solution().max_depth(root)
    print(depth)
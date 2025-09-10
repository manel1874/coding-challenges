"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

from collections import deque
from aux import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res = []

        if not root:
            return res
        
        q = deque([root])
        
        while q:
            same_level = []
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                same_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(same_level)

        return res
    

if __name__ == "__main__":
    lor = [3,9,20,None,None,15,7]
    root = TreeNode.lor2tree(lor)
    res = Solution().levelOrder(root)
    print(res)

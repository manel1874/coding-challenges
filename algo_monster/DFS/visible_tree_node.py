"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""



from aux import TreeNode

class Solution:
    def visible_nodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if node is None:
                return 0
            
            if node.val >= max_val:
                visible = 1
                max_val = node.val
            else:
                visible = 0

            left_nr_visible = dfs(node.left, max_val)
            right_nr_visible = dfs(node.right, max_val)

            return visible + left_nr_visible + right_nr_visible

        return dfs(root, root.val)

if __name__ == "__main__":
    lor = [3,1,4,3,None,1,5]
    root = TreeNode.lor2tree(lor)
    nr_visible = Solution().visible_nodes(root)
    print(nr_visible)

    lor = [3,3,None,4,2]
    root = TreeNode.lor2tree(lor)
    nr_visible = Solution().visible_nodes(root)
    print(nr_visible)


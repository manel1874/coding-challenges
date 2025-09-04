"""A binary tree is considered balanced if, for every node in the tree, the difference in the height (or depth) of its left and right subtrees is at most 1.

In other words, the depth of the two subtrees for every node in the tree differs by no more than one.

The height (or depth) of a tree is defined as the number of edges on the longest path from the root node to any leaf node.

Note: An empty tree is considered balanced by definition.

In that case, given a binary tree, determine if it is balanced.

Parameter
tree: A binary tree.
Result
A boolean representing whether the tree given is balanced.
"""

from aux import TreeNode

class Solution:
    def is_balanced(self, root: TreeNode) -> bool:

        def dfs(node: TreeNode) -> int:
            # DFS will return the height of the current. 
            # At every level we compare the height of both left and right
            # If the the difference is bigger than 1, we return false.
            # We will represent false as -1.
            if node is None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if left_height == -1 or right_height == -1 :
                return -1
            
            if abs(right_height - left_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return dfs(root) != -1

if __name__ == "__main__":
    lor = [3,9,20,None,None,15,7]
    root = TreeNode.lor2tree(lor)
    b = Solution().is_balanced(root)
    print(b)

    lor = [1,2,2,3,3,None,None,4,4]
    root = TreeNode.lor2tree(lor)
    b = Solution().is_balanced(root)
    print(b)

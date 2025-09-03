"""
Let's look at a simple problem of searching for a node in a binary tree whose value is equal to target.
"""
from aux import TreeNode

def dfs(root: TreeNode, target: int) -> TreeNode:

    if root is None:
        return None
    
    if root.val == target:
        return root
    
    return dfs(root.left, target) or dfs(root.right, target)

"""
We want to "pretty-print" the directory structure with indents like this:

/
  foo
    baz
  bar
We can pass the current indent level as a state of the recursive call.
"""

indent_per_level = "    "
def dfs(node: TreeNode, indent_level):
    if node is None:
        return None
    current_indent_level = indent_level + indent_per_level
    print(current_indent_level + node.val)
    dfs(node.left, current_indent_level)
    dfs(node.right, current_indent_level)

"""
Consider the problem of finding the maximum value in a binary tree.
"""

def dfs(node):
    if node is None:
        return None
    left_val = dfs(node.left)
    right_val = dfs(node.right)
    return max(node.val, left_val, right_val)

"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

https://leetcode.com/problems/palindrome-partitioning/
"""


"""
function dfs(start_index, path):
    if is_leaf(start_index):
        report(path)
        return
    for edge in get_edges(start_index):
        # prune if needed
        if not is_valid(edge):
            continue
        path.add(edge)
        # increment start_index
        dfs(start_index + len(edge), path)
        path.pop()
  """

def partition(s):
    def is_palindrome(subs):
        return subs == subs[::-1]

    def backtrack(start, path, result):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(start + end - start, path, result)
                path.pop()

    result = []
    backtrack(0, [], result)
    return result

# Example usage:
print(partition("aab"))  # Output: [["a","a","b"],["aa","b"]]


"""
Given two strings, original and check, return the minimum substring of original such that each character in check, including duplicates, are included in this substring. By "minimum", I mean the shortest substring. If two substrings that satisfy the condition have the same length, the one that comes lexicographically first is smaller.

Parameters
original: The original string.
check: The string to check if a window contains it.
Result
The smallest substring of original that satisfies the condition.
Examples
Example 1
Input: original = "cdbaebaecd", check = "abc"

Output: baec

Explanation: baec is the shortest substring of original that contains all of a, b, and c.

Constraints
1 <= len(check), len(original) <= 10^5
original and check both contain only uppercase and lowercase characters in English. The characters are case sensitive.

https://leetcode.com/problems/minimum-window-substring/description/
"""

from collections import Counter


class Solution:
    def min_window(self, original: str, check: str) -> str:

        check_counter = Counter(check)
        original_window_counter = Counter("")
        l = 0
        min_l = 0
        min_r = 0
        min_len = len(original) + 1
        
        for r, val in enumerate(original):
            original_window_counter[val] += 1

            while original_window_counter >= check_counter:
                current_len = r - l + 1
                if min_len > current_len or (min_len == current_len and original[l] < original[min_l]):
                    min_len = current_len
                    min_l = l
                    min_r = r
                original_window_counter[original[l]] -= 1
                l += 1

        return original[min_l:min_r+1] if min_r != len(original) else original[min_l:]


if __name__ == "__main__":
    original = "cdbaebaecd"
    check = "abc"
    mw = Solution().min_window(original, check)
    print(mw)

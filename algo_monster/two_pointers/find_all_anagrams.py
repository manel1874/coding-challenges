"""
Given a string original and a string check, find the starting index of all substrings of original that is an anagram of check. The output must be sorted in ascending order.

Parameters
original: A string
check: A string
Result
A list of integers representing the starting indices of all anagrams of check.
Examples
Example 1
Input: original = "cbaebabacd", check = "abc"

Output: [0, 6]

Explanation: The substring from 0 to 2, "cba", is an anagram of "abc", and so is the substring from 6 to 8, "bac".

Example 2
Input: original = "abab", check = "ab"

Output: [0, 1, 2]

Explanation: All substrings with length 2 from "abab" are anagrams of "ab".

Constraints
1 <= len(original), len(check) <= 10^5
Each string consists of only lowercase characters in the standard English alphabet.


https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
438
"""

from collections import Counter

def is_anagram(str_a: str, str_b: str) -> bool:
    cnt_a = Counter(str_a)
    cnt_b = Counter(str_b)

    return cnt_a == cnt_b

class Solution:

    def find_anagrams(self, original: str, check: str) -> list[int]:
        
        len_check = len(check)
        len_original = len(original)
        list_idx = []

        if len_original < len_check:
            return list_idx
        
        for l in range(len_original):
            r = l + len_check
            substring = original[l:r]
            if is_anagram(substring, check):
                list_idx.append(l)
        
        return list_idx




if __name__ == "__main__":


    original = "cbaebabacd"
    check = "abc"
    list_idx = Solution().find_anagrams(original, check)
    print(list_idx)

    original = "abab"
    check = "ab"
    list_idx = Solution().find_anagrams(original, check)
    print(list_idx)

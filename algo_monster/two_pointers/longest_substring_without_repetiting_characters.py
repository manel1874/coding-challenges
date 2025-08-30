"""
Find the length of the longest substring of a given string without repeating characters.

Input: abccabcabcc

Output: 3

Explanation: The longest substrings are abc and cab, both of length 3.

Input: aaaabaaa

Output: 2

Explanation: ab is the longest substring, with a length of 2.
"""

from collections import defaultdict

class Solution:
    def find_length_longest_set_based(self, s: str) -> int:
        
        chars = set([])
        len_s = len(s)
        max_len = 0
        l = 0

        for r in range(len_s):

            while s[r] in chars:
                chars.remove(s[l])
                l += 1
        
            chars.add(s[r])
            current_len = r - l + 1
            max_len = max(max_len, current_len)

        return max_len

    def find_length_longest_dict_based_o2(self, s: str) -> int:

        chars_count = defaultdict(int)
        len_s = len(s)
        max_len = 0
        l = 0

        for r in range(len_s):
            while chars_count[s[r]] > 0:
                chars_count[s[l]] -= 1
                l += 1

            chars_count[s[r]] += 1
            current_len = r - l + 1
            max_len = max(max_len, current_len)

        return max_len
    
    def find_length_longest_dict_based_o1(self, s: str) -> int:

        last_seen = {}
        max_len = 0
        l = 0

        for r, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= l:
                l = last_seen[ch] + 1

            last_seen[ch] = r
            current_len = r - l + 1
            max_len = max(max_len, current_len)

        return max_len



if __name__ == "__main__":
    s = "aabcbbb"
    length_set = Solution().find_length_longest_set_based(s)
    length_dict = Solution().find_length_longest_dict_based_o1(s)
    print(length_set)
    print(length_dict)
    print(Solution().find_length_longest_dict_based_o2("abccabcabcc"))  # 3
    print(Solution().find_length_longest_dict_based_o2("aaaabaaa"))     # 2
    print(Solution().find_length_longest_dict_based_o2("abcdef"))       # 6
    print(Solution().find_length_longest_dict_based_o2(""))             # 0  

    print(Solution().find_length_longest_dict_based_o1("abccabcabcc"))  # 3
    print(Solution().find_length_longest_dict_based_o1("aaaabaaa"))     # 2
    print(Solution().find_length_longest_dict_based_o1("abcdef"))       # 6
    print(Solution().find_length_longest_dict_based_o1(""))             # 0  


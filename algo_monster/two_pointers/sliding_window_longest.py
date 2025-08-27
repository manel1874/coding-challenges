"""
sliding window – longest

given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters.

parameters

s: a string

k: an integer

result

an integer representing the length of the longest substring with at most k distinct characters.

examples

input:

s = "eceba", k = 2


output:

3


explanation: the substring "ece" has 2 distinct characters and is the longest.

input:

s = "aa", k = 1


output:

2


explanation: the substring "aa" has 1 distinct character and is the longest.

constraints

1 <= len(s) <= 10^5

s consists of lowercase letters only

1 <= k <= 26

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
"""

from collections import defaultdict

class Solution:
    def find_length_o3(self, s: str, k: int) -> int:
        max_len = 0
        l, r = 0, 0

        # This while loop might repeat in worst case O(n^2) times
        while r < len(s):
            substring = s[l:r+1]                        # creates substring in every loop (O(n))
            distinct_chars = set(substring)             # creates a set in every loop, O(n)
            current_distinct_len = len(distinct_chars)
            if current_distinct_len <= k:
                max_len = max(max_len, len(substring))
                r += 1
            else:
                l += 1
        # Overall complexity is O(n^3)
        return max_len
    

    def find_length_o1(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0
        
        max_len = 0
        l = 0
        char_count = defaultdict(int)

        for r in range(len(s)):

            char_count[s[r]] += 1

            # Shrink window
            while len(char_count) > k:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1

            length_subtring = r - l + 1
            max_len = max(max_len, length_subtring)

        return max_len




if __name__ == "__main__":
    s = "eceba"
    k = 2
    len_o3 = Solution().find_length_o3(s, k)
    print(len_o3)
    len_o1 = Solution().find_length_o1(s, k)
    print(len_o1)

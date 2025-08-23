"""
https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/?envType=daily-question&envId=2025-07-17

You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.
 

Example 1:

Input: nums = [1,2,3,4,5], k = 2

Output: 5

Explanation:

The longest valid subsequence is [1, 2, 3, 4, 5].

Example 2:

Input: nums = [1,4,2,3,1,4], k = 3

Output: 4

Explanation:

The longest valid subsequence is [1, 4, 1, 4].

"""

import numpy as np

class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        
        pp = [ [0] * k for _ in range(k) ]
        res = 0
        for num in nums:
            num %= k 
            for prev in range(k):
                pp[prev][num] = pp[num][prev] + 1         
                res = max(res, pp[prev][num])

        return res
    

if __name__ == "__main__":
    solution = Solution()
    sol = solution.maximumLength([1,2,3,6,23,7,34,78,2,834,4,12,4,67,3,4,745,3456,7,4,5], 3)
    print(sol)




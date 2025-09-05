"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1

https://leetcode.com/problems/sqrtx/
"""

class Solution:
    def my_sqrt(self, x: int) -> int:
        
        l, r = 0, x
        
        while l <= r:
            mid = (l + r) // 2

            if mid**2 == x:
                return mid
            elif mid**2 > x:
                r = mid - 1
            else:
                l = mid + 1

        return r
    

if __name__ == "__main__":
    x = 8
    estimation_sqrt = Solution().my_sqrt(x)
    print(estimation_sqrt)

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
"""

[ 1, 2, 3, 4, 5, 6]

[ 1, 1, 2, 6, 24, 120 ]



class Solution:
    def product_except_self_prefix_and_sufix(self, nums: list[int]) -> list[int]:
        
        len_nums = len(nums)

        # compute prefix and suffix
        prefix_mult = {}
        current_premult = 1
        suffix_mult = {}
        current_sufmult = 1
        for i in range(len_nums):
            current_premult *= nums[i]
            prefix_mult[i] = current_premult
            current_sufmult *= nums[len_nums - 1 - i]
            suffix_mult[len_nums - 1 - i] = current_sufmult

        # compute answer s.t. answer[i] is equal to the product of all the elements
        # of nums except nums[i]
        answer = []
        for i in range(len_nums):
            if i == 0:
                prod = suffix_mult[i+1]
            elif i == len_nums - 1:
                prod = prefix_mult[i-1]
            else:
                prod = prefix_mult[i-1] * suffix_mult[i+1]
            answer.append(prod)

        return answer
    

    def product_except_self(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
    
        return output    

if __name__ == "__main__":
    nums = [1,2,3,4]
    l = Solution().product_except_self_prefix_and_sufix(nums)
    print(l)
    l = Solution().product_except_self(nums)
    print(l)


"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""


class Solution:
    def min_subarray_len(self, nums: list[int], target: int) -> int:
        
        current_sum = 0
        min_length = len(nums) + 1
        l = 0

        for r, val in enumerate(nums):

            current_sum += val

            while current_sum >= target:
                min_length = min(min_length, r - l + 1)
                current_sum -= nums[l]
                l += 1
            
        return 0 if min_length == len(nums) + 1 else min_length


if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    target = 7
    m = Solution().min_subarray_len(nums, target)
    print(m)         


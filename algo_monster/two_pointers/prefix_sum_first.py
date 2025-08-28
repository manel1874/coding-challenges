"""
Given an array of integers and an integer target, find a subarray that sums to target and return the start and end indices of the subarray.

Input: arr: 1 -20 -3 30 5 4 target: 7

Output: 1 4

Explanation: -20 - 3 + 30 = 7. The indices for subarray [-20,-3,30] is 1 and 4 (right exclusive).
"""

class Solution:
    def subarray_sum(self, arr: list[int], target: int) -> list[int]:
        
        current_prefix_sum = 0
        prefix_sum_dict = {0: 0}

        for r, val in enumerate(arr):
            current_prefix_sum += val
            diff = current_prefix_sum - target
            if diff in prefix_sum_dict:
                return [prefix_sum_dict[diff], r + 1]
            
            prefix_sum_dict[current_prefix_sum] = r + 1

        return []
    


    """
    Find the total number of subarrays that sums up to target.
    """
    def subarray_sum_all(self, arr: list[int], target: int) -> int:
        
        prefix_sum_dict = Counter()
        prefix_sum_dict[0] = 1
        current_prefix_sum = 0
        total = 0

        for r, val in enumerate(arr):
            current_prefix_sum += val
            diff = current_prefix_sum - target
            if diff in prefix_sum_dict:
                total += prefix_sum_dict[diff]
            
            prefix_sum_dict[current_prefix_sum] += 1

        return total

from collections import Counter

if __name__ == "__main__":
    arr = [10, 5, -5, -20, 10]
    target = -10
    res = Solution().subarray_sum_all(arr, target)
    print(res)


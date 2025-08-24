"""
Two Sum Sorted
Given an array of integers sorted in ascending order, find two numbers that add up to a given target. Return the indices of the two numbers in ascending order. You can assume elements in the array are unique and there is only one solution. Do this in O(n) time and with constant auxiliary space.

Input:

arr: a sorted integer array
target: the target sum we want to reach
Sample Input: [2, 3, 4, 5, 8, 11, 18], 8

Sample Output: 1 3
"""

class Solution:
    def two_sums(self, nums: list[int], target: int) -> list[int]:

        fast = 1

        for slow in range(len(nums)-1):
            fast = slow + 1
            sum = nums[slow] + nums[fast]
            while sum <= target:
                sum = nums[slow] + nums[fast]
                if sum == target:
                    return [slow, fast]
                fast += 1


        return None


if __name__ == "__main__":
    arr = [2, 3, 4, 5, 8, 11, 18]; target = 8
    mz_arr = Solution().two_sums(arr, target)
    print(mz_arr) 

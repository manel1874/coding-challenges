"""
A sorted array of unique integers was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. Find the index of the minimum element in this array.

Input: [30, 40, 50, 10, 20]

Output: 3

Explanation: The smallest element is 10, and its index is 3.

Input: [3, 5, 7, 11, 13, 17, 19, 2]

Output: 7

Explanation: The smallest element is 2, and its index is 7.
"""

class Solution:
    def min_rot_sort_array_o1(self, arr: list[int]) -> int:

        for i in range(len(arr)):
            if arr[i] - arr[i-1] < 0:
                return i
        return 0
    
    def min_rot_sort_array_olog(self, arr: list[int]) -> int:

        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > arr[-1]:
                l = mid + 1
            else:
                r = mid - 1

        return r



    
if __name__ == "__main__":
    arr =[3, 5, 7, 11, 13, 17, 19, 2]
    idx = Solution().min_rot_sort_array_o1(arr)
    print(idx)
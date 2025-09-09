"""
An array of boolean values is divided into two sections: The left section consists of all false, and the right section consists of all true. Find the First True in a Sorted Boolean Array of the right section, i.e., the index of the first true element. If there is no true element, return -1.

Input: arr = [false, false, true, true, true]

Output: 2

Explanation: The first true's index is 2.
"""


class Solution:
    def first_true(self, arr: list[bool]) -> int:
        
        if all(not val for val in arr):
            return -1

        l, r = 0, len(arr) - 1

        while l <= r: 
            mid = (l + r) // 2
            if arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
    
    def find_boundary(arr: list[bool]) -> int:
        left, right = 0, len(arr) - 1
        boundary_index = -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid]:
                boundary_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return boundary_index


if __name__ == "__main__":
    arr = [False, False, True, True, True]
    val = Solution().first_true(arr)
    print(val)
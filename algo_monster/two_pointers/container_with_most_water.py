"""
container with most water

you are given an array of non-negative integers height, where each element represents a vertical line drawn on the x-axis at that index. two lines, together with the x-axis, form a container.

return the maximum amount of water a container can store.

example:

input: height = [1,8,6,2,5,4,8,3,7]
output: 49

https://leetcode.com/problems/container-with-most-water/description/
"""

def area_of_water(l: int, r: int, idx_l: int, idx_r: int) -> int:
    area = min(l, r) * (idx_r - idx_l)
    return area

class Solution:
    def most_water_o2(self, arr: list[int]) -> int:
        slow, fast = 0, 1
        length = len(arr)
        amount = 0

        for slow in range(length):
            while fast < length:
                area = area_of_water(arr[slow], arr[fast], slow, fast)
                amount = area if area > amount else amount
                fast += 1
            fast = slow + 1

        return amount
    
    def most_water_o1(self, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1
        amount = 0

        while l<r:
            area = min(arr[l], arr[r]) * (r - l)
            amount = max(amount, area)

            if arr[l] < arr[r]:
                l += 1
            else:
                r -= 1

        return amount
    
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    max_area_o2 = Solution().most_water_o2(height)
    max_area_o1 = Solution().most_water_o1(height)
    print("O(n^2) solution: ", max_area_o2)
    print("O(n) solution: ", max_area_o1)
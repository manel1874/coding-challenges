"""
Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of the non-zero elements. Do this in-place using constant auxiliary space.

Input:

[1, 0, 2, 0, 0, 7]
Output:

[1, 2, 7, 0, 0, 0]
"""

class Solution:

    def move_zeros(self, nums: list[int]) -> list[int]:
        length = len(nums)
        j=0

        for _ in range(length):
            if nums[j] == 0:
                del nums[j]
                nums.append(0)
                continue
            j += 1

        return nums

    def move_zeros_opt(self, nums: list[int]) -> list[int]:
        length = len(nums)
        write_pos = 0

        for read_pos in range(length):
            if nums[read_pos] != 0:
                nums[write_pos] = nums[read_pos]
                write_pos += 1

        while write_pos < length:
            nums[write_pos] = 0
            write_pos += 1

        return nums


if __name__ == "__main__":
    arr = [0, 1, 2, 0, 3, 0, 0, 4, 0, 0]
    mz_arr = Solution().move_zeros(arr)
    print(mz_arr)
    mz_arr_opt = Solution().move_zeros_opt(arr)
    print(mz_arr_opt)
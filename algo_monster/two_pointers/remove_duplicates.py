"""
Given a sorted list of numbers, remove duplicates and return the new length. You must do this in-place and without using extra memory.

Input: [0, 0, 1, 1, 1, 2, 2].

Output: 3.

Your function should modify the list in place so that the first three elements become 0, 1, 2. Return 3 because the new length is 3.
"""

class SetSolution:
    def remove_duplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        seen = set()

        for num in nums:
            seen.add(num)

        return len(seen)


class TwoPointersSolutions:
    def remove_duplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        uniq_nums = []
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                right = right+1
            else:
                uniq_nums.append(nums[left])
                left = right
                right = right+1
        uniq_nums.append(nums[left])
        
        return len(uniq_nums)


class InPlaceTwoPointersSolutions:
    def remove_duplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = 1
        len_uniq = 0

        while right < len(nums):
            if nums[left] == nums[right]:
                right = right+1
            else:
                left = right
                right = right + 1
                len_uniq = len_uniq + 1
        
        return len_uniq + 1



if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4]
    print(SetSolution().remove_duplicates(nums))
    print(TwoPointersSolutions().remove_duplicates(nums))
    print(InPlaceTwoPointersSolutions().remove_duplicates(nums))
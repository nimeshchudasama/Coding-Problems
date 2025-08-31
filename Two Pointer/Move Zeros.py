"""
Given an integer array nums, write a function to rearrange the array by moving all zeros
to the end while keeping the order of non-zero elements unchanged.

Perform this operation in-place without creating a copy of the array
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        insertion_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[insertion_index] = nums[insertion_index], nums[i]
                insertion_index += 1

        return nums
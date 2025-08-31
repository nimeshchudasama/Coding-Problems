"""
Given an input integer array nums, write a function to find all unique triplets
[nums[i], nums[j], nums[k]] such that i, j, and k are distinct indices, and the
sum of nums[i], nums[j], and nums[k] equals zero. Ensure that the resulting list
does not contain any duplicate triplets.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]):
        # Sorting so we can use two pointer, dont have to check
        # everything
        nums.sort()

        # Using a variable to store instead of computing
        # len(nums) for the right pointer in the for range
        len_of_nums = len(nums)

        # Answer array to return
        answers = []

        # For loop only extends to len - 2 because the last iteration is
        # one triple to check
        for i in range(len_of_nums - 2):
            # Skips processing duplicate pairs e.g. [-1, -1, 0, 1]
            # If we didn't have this there would be two -1, 0, 1
            # in answer array
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            current_num = nums[i]
            left = i + 1
            right = len_of_nums - 1

            # Classic two pointer technique
            while left < right:
                left_number = nums[left]
                right_number = nums[right]
                current_sum = current_num + left_number + right_number
                # If it satisfies the condition, append to answer
                if current_sum == 0:
                    answers.append([current_num, left_number, right_number])
                    # Check left < right first otherwise left + 1 could get a bounds issue
                    # This while loop skips duplicate left values to avoid same answer being appended
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Check left < right first otherwise right - 1 could get a bounds issue
                    # This while loop skips duplicate right values to avoid same answer being appended
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return answers
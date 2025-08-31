"""
Write a function to sort a given integer array nums in-place
(and without the built-in sort function), where the array contains n integers
that are either 0, 1, and 2 and represent the colors red, white, and blue.

Arrange the objects so that same-colored ones are adjacent, in the order of red, white, and blue (0, 1, 2).
"""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]):
        i = 0
        left_insertion = 0                 # where the next 0 should be placed
        right_insertion = len(nums) - 1    # where the next 2 should be placed

        # Keep scanning until i passes the right boundary
        while i <= right_insertion:
            if nums[i] == 0:
                # Case 1: current value is 0
                # Swap it to the "left side" where 0s belong
                nums[i], nums[left_insertion] = nums[left_insertion], nums[i]

                # We've placed a 0, so advance both:
                # - left_insertion moves right (next slot for 0)
                # - i moves right (continue scanning forward)
                left_insertion += 1
                i += 1

            elif nums[i] == 2:
                # Case 2: current value is 2
                # Swap it to the "right side" where 2s belong
                nums[i], nums[right_insertion] = nums[right_insertion], nums[i]

                # We've placed a 2, so move right_insertion left
                right_insertion -= 1

                # BUT: don't move i yet!
                # The element swapped in from the right could be 0, 1, or 2.
                # We need to examine it in the next loop iteration.

            else:
                # Case 3: current value is 1
                # 1s belong in the middle, so leave it in place.
                # Just move i forward.
                i += 1

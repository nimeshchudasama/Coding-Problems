"""
Write a function to return the length of the longest substring in a
provided string s where all characters in the substring are distinct.
"""

class Solution:
    def longestSubstringWithoutRepeat(self, s: str):
        chars_in_substring = {}
        max_length = 0
        start = 0
        for idx, val in enumerate(s):
            chars_in_substring[val] = chars_in_substring.get(val, 0) + 1
            while chars_in_substring[val] > 1:
                chars_in_substring[s[start]] -= 1
                start += 1
            max_length = max(max_length, idx - start + 1)

        return max_length
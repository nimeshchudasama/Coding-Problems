"""
Write a function to find the length of the longest substring containing the same
letter in a given string s, after performing at most k operations in which you
can choose any character of the string and change it to any other uppercase English letter.
"""

class Solution:
    def characterReplacement(self, s: str, k: int):
        start = 0
        max_length = 0
        max_freq = 0
        counts = {}

        for idx, val in enumerate(s):
            counts[val] = counts.get(val, 0) + 1
            max_freq = max(max_freq, counts[val])
            current_length = idx - start + 1
            while current_length - max_freq > k:
                counts[s[start]] -= 1
                start += 1
                current_length -= 1
            max_length = max(current_length, max_length)
        return max_length
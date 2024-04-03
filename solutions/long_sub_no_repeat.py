# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1222221351/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left      = 0
        longest   = 0
        substring = set()

        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1

            substring.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
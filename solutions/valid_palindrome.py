# https://leetcode.com/submissions/detail/1211237537/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = ""
    
        for c in s:
            if c.isalnum():
                alpha_s += c.lower()

        return bool(alpha_s == alpha_s[::-1])
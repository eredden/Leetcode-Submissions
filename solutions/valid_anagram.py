# https://leetcode.com/submissions/detail/1208628465/

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t) 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}

        for char in s: 
            if not char in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

        for char in t: 
            try:
                char_count[char] -= 1
            except:
                return False

        for char in char_count:
            if char_count[char] != 0:
                return False
        
        return True
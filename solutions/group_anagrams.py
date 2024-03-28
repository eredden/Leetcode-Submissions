# https://leetcode.com/submissions/detail/1209520122/

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for anagram in strs:
            # good practice? no. blazingly fast? yes.
            anagrams[ str(sorted(anagram)) ].append(anagram)
        
        return anagrams.values()
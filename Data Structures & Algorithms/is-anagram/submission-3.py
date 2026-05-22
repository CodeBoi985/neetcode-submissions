class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = sorted(s) == sorted(t)
        return is_anagram
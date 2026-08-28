class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        seek_anagram = dict()

        for char in s:
            seek_anagram[char] = seek_anagram.get(char, 0) + 1
        
        for char in t:
            if char not in seek_anagram or seek_anagram[char] == 0:
                return False
            seek_anagram[char] -= 1

        return True
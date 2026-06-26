class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ###ONE LINE OF CODE and is cheating

        if Counter(s) == Counter(t):
            return True
        return False
        

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ###SORTING METHOD , not as efficient

        return sorted(s) == sorted(t)
        

        
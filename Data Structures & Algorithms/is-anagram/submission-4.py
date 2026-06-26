class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counter = {}


        for letter in s:

            if letter in counter:
                counter[letter] += 1

            else:
                counter[letter] = 1

        for letter in t:
            
            if letter in counter:
                counter[letter] -= 1
            else:
                return False

        for k in counter:
            if counter[k] != 0:
                return False
        
        return True
        

        
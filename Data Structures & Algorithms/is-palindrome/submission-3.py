class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s)-1
        i = 0

        while i < j :
            left = s[i].lower()
            if left.isalnum() is False:
                i+=1
                continue
            
            right = s[j].lower()
            if right.isalnum() is False:
                j-=1 
                continue

            
            if right != left:
                return False

            i+=1
            j-=1

        return True
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        while i<j:
            
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



        
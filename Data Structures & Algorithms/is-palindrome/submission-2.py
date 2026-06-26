class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        while i<j:
            
            left = s[i].lower()
            if self.alphaNum(left) is False:
                i+=1
                continue

            right = s[j].lower()
            if self.alphaNum(right) is False:
                j-=1
                continue
            
            if right != left:
                return False
            i+=1
            j-=1
            

        return True

    def  alphaNum(self,c):
        return (ord('A') <= ord(c) <= ord("Z")or
        ord('a') <= ord(c) <= ord("z")or
        ord('0') <= ord(c) <= ord("9"))



        
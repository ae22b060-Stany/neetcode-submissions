class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac_hash = {')' :"(" ,"}":"{" , "]" :"["}

        for ch in s :
            if ch in brac_hash:
                if stack and stack[-1] == brac_hash[ch]:
                    stack.pop()
                else:
                    return False

            else :
                stack.append(ch)
        return True if not stack else False



            
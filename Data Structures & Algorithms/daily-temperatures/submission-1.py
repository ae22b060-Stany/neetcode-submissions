class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        if len(temperatures)==1:
            return [0]

        l = 0
        r = 1

        c = 0

        for l in range(len(temperatures)) :
            c = 0
            found = False
            for r in range(l+1, len(temperatures)):
                if temperatures[r] <= temperatures[l]:
                    c +=1
                    continue
                else:
                    c+=1
                    found = True
                    res.append(c)
                    break
            if not found:
                res.append(0)

        return res

        
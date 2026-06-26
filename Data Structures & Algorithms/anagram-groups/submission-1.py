class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)# We create a defaultdict where each default value is an empty list (list()).

        for s in strs:
            count =[0] * 26 # a to z

            for c in s:
                count[ord(c) - ord('a')] +=1
            res[tuple(count)].append(s)

        return res.values()

        


            
##############THIS solution has time complexity of O( mn) 

        
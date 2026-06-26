class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedstrs = ["".join(sorted(string)) for string in strs] ###[sorted(string) for string in strs] gives a list of lists, thats the error

        hashmap = {}

        for i in range(len(strs)):
            
            if sortedstrs[i] not in hashmap:
                hashmap[sortedstrs[i]] = [strs[i]]
            else:
                hashmap[sortedstrs[i]].append(strs[i])

        return [hashmap[x] for x in hashmap]

            


        
class Solution: # BRUTE FORCE
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums) - 2):
            n1 = nums[i]
            for j in range(i+1, len(nums) -1):
                n2 = nums[j]
                for k in range(j+1, len(nums)):
                    n3 = nums[k]

                    if n1 + n2 + n3 == 0:
                        newSet = (sorted([n1,n2,n3]))
                        if newSet not in output:
                            output.append(newSet)
        
        return output

        
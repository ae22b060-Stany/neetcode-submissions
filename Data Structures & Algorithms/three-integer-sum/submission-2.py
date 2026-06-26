class Solution: #Most optimal solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i, v in enumerate(nums):

            if i>0 and nums[i-1] == v:
                continue # This is for avoiding duplicates in the first column. 


            # now we go for two sum

            l,r = i+1 , len(nums) -1 

            while l<r : # Since left and right canNOT be equal(Distinct)

                if v + nums[l] + nums[r] == 0 :
                    res.append([v,nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

                elif v + nums[l] + nums[r]> 0:
                    r-=1
                else:
                    l+=1
                # Now since there are duplicates , we need to handle them!

                

        return res



        
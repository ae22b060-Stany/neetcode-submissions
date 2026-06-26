class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ###using division operator
        output = [1 for x in nums]
        
        for i  in range(len(nums) ):

            
            output[:i]  = [output[j] * nums[i] for j in range(0,i) ]
            if i < len(nums) -1:
                output[i+1 :] = [output[j] * nums[i] for j in range(i+1,len(nums))]

        return output
        
        
                
            
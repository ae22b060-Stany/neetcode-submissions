class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        counter = 1
        max_c = 1
        if not nums:
            return 0

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            
            if nums[i+1] - nums[i] == 1:
                counter+=1
            else:
               # max_c = max(max_c, counter)
                counter = 1
                continue
            max_c = max(max_c, counter)
        return max_c

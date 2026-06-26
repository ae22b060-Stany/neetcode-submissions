class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        



        l = 0
        r = len(nums) - 1
                # Array is already sorted
        if nums[l] < nums[r]:
            return nums[l]

        minim = nums[(l + r)//2]
        while l <= r :
            mid = (l + r)//2

            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            elif nums[mid-1]  > nums[mid] :
                return nums[mid]
            elif nums[mid] > nums[r]:
                l = mid +1
                r = r
            else:
                l  = l
                r = mid -1


            
        return nums[mid]
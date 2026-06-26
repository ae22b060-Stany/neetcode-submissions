class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i , j = 0 , len(numbers) -1
        while i < j :

            left = numbers[i]
            right = numbers[j]

            req = target - left

            if req == right :
                return [i+ 1 , j+1]

            elif req > right:
                i+=1
                
            else :
                j-=1
                

        
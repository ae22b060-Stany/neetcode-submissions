class Solution:
    def maxArea(self, heights: List[int]) -> int:
        A_max = 0
        for i in range(len(heights)):

            for j in range(len(heights)-1 ,0 ,-1):

                A = min(heights[i],heights[j] )* (j-i)
                if A > A_max:
                    A_max = A

        return A_max
        
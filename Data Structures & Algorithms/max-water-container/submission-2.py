class Solution:
    def maxArea(self, heights: List[int]) -> int:
        A_max = 0
        
        i = 0
        j = len(heights) - 1

        while i < j:
            area = (j-i) * min(heights[i], heights[j])
            A_max = max(area, A_max)

            if heights[j]< heights[i]:
                j-=1
            else:
                i+=1

        return A_max

        
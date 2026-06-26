class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        collector = []
        for item in nums:
            if item in collector:
                return True
            else:
                collector.append(item)
        return False

            
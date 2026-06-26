class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        bucket = []
        counter =  dict(Counter(nums))
        reverse_counter = {}

        for num, freq in counter.items():

            if freq in reverse_counter:
                reverse_counter[freq].append(num)

            else:
                reverse_counter[freq] = [num]

        reverse_counter = dict(reversed(sorted(reverse_counter.items())))

        req_list = list(reverse_counter.values())
        i = 0 
        while i< len(req_list):

            bucket.extend(req_list[i])
            k-= len(req_list[i])
            i+= 1

            if k < 1:
                break
            

        return bucket
            











class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        
        val = []

        while k > 0:
            maxKey = 0
            max = -1
            for key in count:
                if count[key] > max:
                    max = count[key]
                    maxKey = key
                
            val.append(maxKey)
            count.pop(maxKey)
            k -= 1
        
        return val
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        topKheap = []
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1
        for key, value in num_dict.items():
            heapq.heappush(topKheap,(value,key))
            if len(topKheap) > k:
                heapq.heappop(topKheap)
        ans = []
        for i in topKheap:
            ans.append(i[1])
        return ans

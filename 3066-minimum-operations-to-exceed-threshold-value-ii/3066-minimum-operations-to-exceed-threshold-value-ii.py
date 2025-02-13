class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_val = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_val)
            operations += 1   
        return operations
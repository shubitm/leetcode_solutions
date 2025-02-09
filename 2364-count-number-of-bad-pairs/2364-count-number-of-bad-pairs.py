class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        total_pairs = len(nums) * (len(nums) - 1) // 2
        good_pairs = 0
        for i, num in enumerate(nums):
            value = num - i
            good_pairs += freq[value]
            freq[value] += 1
        return total_pairs - good_pairs

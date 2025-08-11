class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False  # Stuck before reaching this index
            max_reach = max(max_reach, i + jump)
        return True

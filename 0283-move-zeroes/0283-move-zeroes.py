class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for num in nums:
            if num != 0:
                nums[left] = num
                left += 1
        for i in range(left, len(nums)):
            nums[i] = 0
        
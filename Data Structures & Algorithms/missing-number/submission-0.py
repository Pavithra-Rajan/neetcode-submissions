class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = nums[0] ^ 0
        for i in range(1, len(nums)):
            res = res ^ nums[i] ^ i 
        res  = res ^ len(nums)
        return res
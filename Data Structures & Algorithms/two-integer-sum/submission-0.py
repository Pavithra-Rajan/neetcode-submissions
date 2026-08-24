class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        maps = {}
        for i in range(len(nums)):
            if target - nums[i] not in maps:
                maps[nums[i]] = i
            else:
                return [maps[target - nums[i]], i]



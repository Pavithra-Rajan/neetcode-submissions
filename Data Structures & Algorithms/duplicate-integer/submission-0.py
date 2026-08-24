class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=Counter(nums)
        for i in hashset.values():
            if i>1:
                return True
        return False
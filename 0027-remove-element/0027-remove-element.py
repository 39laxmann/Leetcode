class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        for i in reversed(range(len(nums))):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)
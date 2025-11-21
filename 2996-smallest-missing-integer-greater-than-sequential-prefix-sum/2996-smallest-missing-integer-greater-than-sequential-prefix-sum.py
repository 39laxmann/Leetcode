class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                total += nums[i]
            else:
                break

        x = total
        num_set = set(nums)
        
        while x in num_set:
            x += 1
        return x

            



        
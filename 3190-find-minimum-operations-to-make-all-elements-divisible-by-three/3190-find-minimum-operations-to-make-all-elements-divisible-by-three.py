class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(1 for x in nums if x % 3 != 0)


        




        
        
        
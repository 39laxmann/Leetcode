class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operation = 0
        if all(x % 3 == 0 for  x in nums):
            return 0
        else:
            not_divisible = [x for x in nums if x % 3 != 0]
            for i in range(len(not_divisible)):
                operation = operation + 1
            return operation


        




        
        
        
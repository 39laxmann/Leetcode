class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        bool_arr = []
        nums_str = ""
        

        for i in range(0,len(nums)):
            nums_str +=str(nums[i])

            if int(nums_str, 2) % 5 == 0:
                bool_arr.append(True)
            else:
                bool_arr.append(False)
            
            
        return bool_arr
        